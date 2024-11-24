import psutil
import time
from datetime import datetime
from plyer import notification

# Function to monitor system health
def monitor_system():
    CPU_THRESHOLD = 90  # Alert if CPU usage exceeds 90%
    MEMORY_THRESHOLD = 80  # Alert if memory usage exceeds 80%
    DISK_THRESHOLD = 80  # Alert if disk usage exceeds 80%

    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        # Print metrics to the terminal
        print(f"{timestamp} | CPU: {cpu_usage}% | Memory: {memory}% | Disk: {disk}%")

        # Save metrics to a log file
        with open("system_health.log", "a") as log_file:
            log_file.write(f"{timestamp} | CPU: {cpu_usage}% | Memory: {memory}% | Disk: {disk}%\n")

        # Trigger notifications if thresholds are exceeded
        if cpu_usage > CPU_THRESHOLD:
            send_alert("High CPU Usage", f"CPU usage is at {cpu_usage}%!")
        if memory > MEMORY_THRESHOLD:
            send_alert("High Memory Usage", f"Memory usage is at {memory}%!")
        if disk > DISK_THRESHOLD:
            send_alert("High Disk Usage", f"Disk usage is at {disk}%!")

        time.sleep(5)  # Wait 5 seconds before checking again

# Function to send notifications
def send_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="System Health Monitor",
        timeout=10  # Notification duration in seconds
    )

# Run the monitor function
if __name__ == "__main__":
    print("Starting System Health Monitor...")
    monitor_system()