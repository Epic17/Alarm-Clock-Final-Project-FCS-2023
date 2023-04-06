import time
import winsound
import datetime

def alarm(set_alarm_timer):
    print("Your alarm has been set for:", set_alarm_timer)
    while True:
        time.sleep(1)
        c_time = datetime.datetime.now()
        current_time = c_time.strftime("%H:%M:%S")
        if current_time == set_alarm_timer:
            print("Time to wake up!")
            winsound.PlaySound("Alarm03.wav",winsound.SND_ASYNC)
            break

print("Welcome to the alarm clock!")
hour = input("Enter the hour (in 24-hour format): ")
minute = input("Enter the minute: ")
second = input("Enter the second: ")
alarm_time = f"{hour}:{minute}:{second}"

alarm(alarm_time)
