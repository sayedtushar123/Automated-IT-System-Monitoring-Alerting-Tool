=====================================================
 Automated IT System Monitoring & Alerting Tool
=====================================================

This tool checks your computer's CPU, Memory, Disk usage,
and important Windows services.  
It sends alerts to your Email and Slack when something is wrong.

-----------------------------------------------------
 1) REQUIREMENTS
-----------------------------------------------------
- Windows 10 or 11
- Python 3 installed (check by running: python --version)
- Internet connection
- A Slack Webhook URL (if using Slack)
- An Email account (e.g., Gmail with an App Password)

-----------------------------------------------------
 2) DOWNLOAD PROJECT
-----------------------------------------------------
Option A: Download ZIP
- Go to the GitHub repository
- Click "Code" → "Download ZIP"
- Unzip it anywhere (example: Desktop)

Option B: Using Git (advanced)
- Open PowerShell
- Run:
    git clone https://github.com/sayedtushar123/system-monitoring-alerting-tool.git
    cd system-monitoring-alerting-tool

-----------------------------------------------------
 3) INSTALL DEPENDENCIES
-----------------------------------------------------
### Normal way
Open PowerShell in the project folder and run:

    pip install -r requirements.txt

### If this does NOT work, use a virtual environment:
1. Create a virtual environment:
    python -m venv venv

2. Activate it:
    .\venv\Scripts\activate

3. Install dependencies inside venv:
    pip install -r requirements.txt

*Now every time you want to run the tool, activate the venv first.*

-----------------------------------------------------
 4) CONFIGURE SETTINGS
-----------------------------------------------------
1. Copy the example config file:

    Copy-Item .\config_example.py .\config.py

2. Edit config.py and fill in your details:
   - CPU, Memory, Disk thresholds
   - Email (sender, password, receiver)
   - Slack webhook URL

IMPORTANT: Keep config.py private. Do not share it online.

-----------------------------------------------------
 5) RUN THE TOOL
-----------------------------------------------------
Run once:
    python .\monitor.py

Run in a loop (every 60 seconds):
    while ($true) { python .\monitor.py; Start-Sleep -Seconds 60 }

Run in the background:
    Start-Job -ScriptBlock { while ($true) { python "$PWD\monitor.py"; Start-Sleep -Seconds 60 } }

If using virtual environment:
    .\venv\Scripts\activate
    python .\monitor.py

-----------------------------------------------------
 6) TESTING ALERTS
-----------------------------------------------------
To test alerts, lower thresholds in config.py:

    CPU_THRESHOLD = 1
    MEMORY_THRESHOLD = 1
    DISK_THRESHOLD = 1

Then run:
    python .\monitor.py

You should get both Slack and Email alerts.

-----------------------------------------------------
 7) AUTOMATE WITH TASK SCHEDULER
-----------------------------------------------------
1. Open Windows Task Scheduler
2. Create a new task:
   - Trigger: Run every 5 minutes
   - Action: Start a program
   - Program/script: powershell.exe
   - Add arguments:
       -NoProfile -ExecutionPolicy Bypass -Command "cd 'C:\Path\To\system-monitoring-alerting-tool'; python .\monitor.py"

3. Save the task.
4. Right-click the task → Run (to test).

If using virtual environment:
   - Change the Task Scheduler "Action" to:
       "C:\Path\To\system-monitoring-alerting-tool\venv\Scripts\python.exe monitor.py"

-----------------------------------------------------
 8) LOGS
-----------------------------------------------------
Logs are saved in:
    logs\monitor.log

View logs live in PowerShell:
    Get-Content .\logs\monitor.log -Wait

-----------------------------------------------------
 9) TROUBLESHOOTING
-----------------------------------------------------
- "python not recognized":
   → Reopen PowerShell, or try "py .\monitor.py"
- Dependencies not installing:
   → Use the virtual environment method above
- Slack alerts not working:
   → Check your Slack webhook URL
- Email not working:
   → Use App Password if using Gmail
- Permission error:
   → Run PowerShell as Administrator

=====================================================
 End of User Guide
=====================================================
