# monitor.py
# System Health Monitor - Checks CPU, Memory, Disk usage, key Windows services,
# and sends alerts via email if thresholds are exceeded.

#slack
from slack_sdk.webhook import WebhookClient
from config import SLACK_WEBHOOK_URL

import psutil
import subprocess
import logging
import os
import smtplib
import socket                            #  Added to get hostname
from email.message import EmailMessage
from config import (
    CPU_THRESHOLD,
    MEMORY_THRESHOLD,
    DISK_THRESHOLD,
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER
)

# Setup logging - logs go to logs/monitor.log
log_file = os.path.join("logs", "monitor.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Slack alert sender
def send_slack_alert(message):
    webhook = WebhookClient(SLACK_WEBHOOK_URL)
    response = webhook.send(text=message)
    if response.status_code == 200:
        print("Slack alert sent.")
    else:
        print(f"Slack alert failed: {response.status_code}")

# Check current CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        return f"High CPU usage detected: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)"
    return None

# Check current memory usage
def check_memory():
    memory_usage = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        return f"High memory usage detected: {memory_usage}% (Threshold: {MEMORY_THRESHOLD}%)"
    return None

# Check current disk usage
def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    print(f"Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        return f"Disk usage is too high: {disk_usage}% (Threshold: {DISK_THRESHOLD}%)"
    return None

# Check if essential Windows services are running
def check_services():
    critical_services = [
        "Spooler",       # Print service
        "wuauserv",      # Windows Update
        "WinDefend",     # Windows Defender
        "BITS",          # Background Intelligent Transfer Service
        "Dhcp",          # DHCP client
        "TermService",   # Remote Desktop
        "EventLog"       # Windows Event Logging
    ]

    service_alerts = []
    print("\nService Status Check:")
    
    for service in critical_services:
        try:
            output = subprocess.check_output(f"sc query {service}", shell=True).decode()
            if "RUNNING" not in output:
                print(f"- Service '{service}' is NOT running.")
                service_alerts.append(f"Service '{service}' is not running.")
            else:
                print(f"- Service '{service}' is running.")
        except subprocess.CalledProcessError:
            print(f"- Service '{service}' not found.")
            service_alerts.append(f"Service '{service}' not found.")

    return service_alerts

# Send an email with the alert message
def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email alert sent.")
    except Exception as e:
        print(f"Error sending email: {e}")
        logging.error(f"Email sending failed: {e}")

# Run all checks and trigger alerts if needed
def run_checks():
    print("Running system health checks...\n")
    alerts = []
    hostname = socket.gethostname()                      #  Get machine name

    # Run all hardware checks
    for check in [check_cpu, check_memory, check_disk]:
        result = check()
        if result:
            alerts.append(result)

    # Check Windows services
    service_warnings = check_services()
    alerts.extend(service_warnings)

    # Handle results
    if alerts:
        print("\nALERTS:")
        for alert in alerts:
            print(f" - {alert}")
        message_body = f" Alert from {hostname} \n\n" + "\n".join(alerts)
        subject = f"[{hostname}] System Monitor Alert"
        send_email(subject, message_body)
        send_slack_alert(message_body)
        logging.warning("Alerts triggered:\n" + message_body)
    else:
        print("\nAll systems are operating within normal parameters.")
        logging.info("System is healthy.")

# Main entry point
if __name__ == "__main__":
    run_checks()
