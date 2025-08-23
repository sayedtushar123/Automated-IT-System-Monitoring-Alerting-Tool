Automated IT System Monitoring & Alerting Tool

Overview

This project is a Python-based monitoring tool designed for IT system administrators.  

It monitors CPU, Memory, Disk usage, and Windows services, and sends real-time alerts via Slack and Email when issues are detected.  

All events are logged for auditing, and the tool can be automated with Windows Task Scheduler.

Features

✅ Monitors CPU, Memory, and Disk thresholds

✅ Checks status of critical Windows services

✅ Sends alerts when thresholds are exceeded:

 - 📧 Email (SMTP)
 - 💬 Slack (Webhook)

✅ Logs all activity into `logs/monitor.log`

✅ Can run continuously or on schedule (Task Scheduler)


Tech Stack

- Python 3

- [psutil](https://pypi.org/project/psutil/) – system monitoring

- [slack\_sdk](https://pypi.org/project/slack-sdk/) – Slack alerts

- smtplib (Python standard library) – email

- logging (Python standard library) – logging




Usage

Clone this repository:
git clone https://github.com/sayedtushar123/Automated-IT-System-Monitoring-Alerting-Tool.git



