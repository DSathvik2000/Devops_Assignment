import psutil
import time

CPU_THRESHOLD = 80

def monitor_cpu():
    print("Monitoring CPU usage... Press Ctrl+C to stop.\n")
    
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            
            if cpu_usage > CPU_THRESHOLD:
                print(f" Alert! CPU usage exceeds threshold: {cpu_usage}%")
            
            time.sleep(1)  
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f" An error occurred: {e}")

monitor_cpu()
