# Automated IT System Monitoring & Alerting Tool  

## 📌 Overview  
This project is a Python-based monitoring tool designed for IT system administrators.  

It continuously monitors CPU, Memory, Disk usage, and critical Windows services, and sends real-time alerts via Slack and Email when issues are detected.  
All activities are logged for auditing, and the tool can be automated with Windows Task Scheduler.  

---

## ✨ Features  
- ✅ Monitor CPU, Memory, and Disk thresholds  
- ✅ Check status of critical Windows services (Spooler → Print,wuauserv → Windows Update service, WinDefend → Windows Defender,BITS → Background Intelligent Transfer Service) 
- ✅ Send alerts when thresholds are exceeded:  
  - 📧 Email (SMTP)  
  - 💬 Slack (Webhook)  
- ✅ Log all activity into `logs/monitor.log`  
- ✅ Run continuously or on schedule (Task Scheduler)  

---

## 🛠️ Tech Stack  
- Python 3.x  
- psutil – system monitoring  
- slack_sdk – Slack alerts  
- smtplib (Python standard library) – email alerts  
- logging (Python standard library) – auditing logs  

---

## 🚀 Installation  

Clone the repository:  
```bash
git clone https://github.com/sayedtushar123/Automated-IT-System-Monitoring-Alerting-Tool

(Optional) Create a virtual environment:  
```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:  
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage  

Run the monitor:  
```bash
python monitor.py
```

All logs will be saved in:  
```
logs/monitor.log
```

---

## ⚡ Example Alerts  

### 📧 Email Alert  
- Subject: ALERT: High CPU Usage  
- Message: CPU usage exceeded 85% on HOSTNAME  

### 💬 Slack Alert  
```
🚨 ALERT: Service 'wuauserv' is not running.
```

---

## 🔄 Automation (Optional)  

You can configure the script to run automatically using Windows Task Scheduler:  
1. Open Task Scheduler  
2. Create a new task → set trigger (e.g., every 5 minutes)  
3. Action → Start a program → point to `python.exe`  
4. Add script path: `monitor.py`  

---

## 📂 Logs for Auditing  
All monitoring activity is stored in `logs/monitor.log`.  
This file can be used for auditing, troubleshooting, and historical review.  
