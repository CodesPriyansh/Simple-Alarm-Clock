import datetime 
import time 

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime(("%H:%M:%S"))
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            break 
        else:
            print(f"current time: {current_time}, waiting for the alarm...")
            time.sleep(1)
    
    


def main():
    print("Simple Alarm Clock")
    alarm_hour = int(input("Enter the hour (0-23) for the alarm:"))
    alarm_minute = int(input("Enter the minute (0-59) for the alarm:"))
    alarm_time = f"{alarm_hour}:{alarm_minute}:00"
    set_alarm(alarm_time)
    print(f"Alarm set for: {alarm_time}")

main() 