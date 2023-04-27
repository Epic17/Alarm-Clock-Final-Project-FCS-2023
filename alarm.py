import time
import winsound
import datetime

def get_time():
    print("Welcome to the alarm clock!")
    while True:
        try:
            hour = int(input("Enter the hour (in 12-hour format): "))
            try:
                if 13 > hour > 0:
                    am_pm = input("AM or PM? ")
                    if am_pm in ["PM", "pm", "Pm", "pM"]:
                        if 12 > hour > 0:
                            hour += 12
                            break
                        else:                                    
                            break
                    elif am_pm in ["AM", "am", "Am", "aM"]:
                        if hour == 12:
                            hour = 24
                            break
                        else:
                            break
                    else:
                        print("Please enter AM or PM.")
                        continue
                else:
                    print("Please enter a number between 1 and 12.")
                    continue
            except:
                print("Please enter a number between 1 and 12.")
                continue
        except:
            print("Please enter the hour in 12-hour format.")
            continue
        
    while True:    
        try:
            minute = int(input("Enter the minute: "))
            if 60 >= minute >= 10:
                print(minute)
                break
            elif 10 > minute >= 0:
                fin_min = minute + "0"
                print(minute)
                print(fin_min)
                break
        except:
            print("Please enter a number between 0 and 60.")
            continue
    
    second = int(input("Enter the second: "))
    
    global alarm_time
    alarm_time = f"{hour}:{fin_min}:{second}"
    
    
    
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



get_time()
alarm(alarm_time)
