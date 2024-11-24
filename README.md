# -real_time_system_monitor-Mac-OS-
A Python-based tool for macOS to monitor CPU, memory, and disk usage in real-time.
# macOS System Monitor

A Python-based tool specifically designed for macOS to monitor system performance in real-time. This script tracks CPU, memory, and disk usage, provides real-time updates in the terminal, logs metrics to a file, and sends macOS desktop notifications when usage exceeds defined thresholds.

---

## Features

- **Real-Time Monitoring**: Tracks CPU, memory, and disk usage every 5 seconds.
- **Alerts**: Sends macOS desktop notifications if usage exceeds the thresholds (default: CPU > 90%, Memory > 80%, Disk > 80%).
- **Logging**: Saves all system metrics to a log file (`system_health.log`).
- **Customizable**: Easily adjust thresholds in the script to suit your needs.

---

## Requirements

1. **macOS** (tested on macOS Big Sur and later).
2. **Python 3.7 or higher** installed.
3. Required Python libraries

   	Open your terminal and navigate to the directory containing the script:
   cd /path/to/macos_system_monitor

   Run the script:
   python3 macos_system_monitor.py
   Expected Outputs:
   2024-11-24 13:00:00 | CPU: 15% | Memory: 40% | Disk: 50%
   Logs will be saved to system_health.log.
	•	Notifications will appear if thresholds are exceeded.

Adjust Thresholds

You can modify CPU, memory, and disk usage thresholds by editing the script:

CPU_THRESHOLD = 90  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 80  # Disk usage percentage

Tips and Tricks
Tip 1: Ensure Python 3 is Installed
Check your Python version by running:
python3 --version

Tip 2: Verify Libraries Are Installed
If the script doesn’t run, ensure the required libraries (psutil, plyer) are installed:

python3 -m pip install psutil plyer

Tip 3: Check for Log Files
The script saves logs to system_health.log. If this file gets too large, delete it periodically.
	•	Tip 4: Use the Correct Interpreter
If the script doesn’t recognize psutil or plyer, ensure you’re using the correct Python interprete
which python3

Tip 5: Add a Cron Job
If you want the script to run automatically at startup, consider creating a macOS cron job or LaunchDaemon.

Troubleshooting

	1.	Error: ModuleNotFoundError
	•	Ensure libraries are installed using:

 python3 -m pip install psutil plyer
 Error: Permission Denied
	•	Ensure the script has execute permissions:

 Desktop Notifications Not Appearing
	•	Make sure macOS notifications are enabled for Python apps in System Preferences > Notifications.

 
