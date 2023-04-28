import time
import datetime
import winsound

def get_time():
    print("Welcome to the alarm clock!")
    
    while True:
        try:
            hour = int(input("Enter the hour (in 12-hour format): "))
            if 13 > hour > 0:
                break
            else:
                print("Please enter a number between 1 and 12.")
                continue
        except:
            print("Please enter the hour in 12-hour format.")
            continue
    
    while True:
        am_pm = input("AM or PM? ")
        if am_pm in ["PM", "pm", "Pm", "pM"]:
            if 12 > hour > 0:
                hour += 12
                break
            else:                                    
                break
        elif am_pm in ["AM", "am", "Am", "aM"]:
            if hour == 12:
                hour = "00"
                break
            else:
                break
        else:
            print("Please enter AM or PM.")
            continue
    
    while True:    
        try:
            minute = int(input("Enter the minute: "))
            if 60 >= minute >= 10:
                fin_min = minute
                break
            elif 10 > minute >= 0:
                fin_min = f"0{minute}"
                break
        except:
            print("Please enter a number between 0 and 60.")
            continue
    
    while True:
        try:
            second = int(input("Enter the second: "))
            if 60 >= second >= 10:
                fin_sec = second
                break
            elif 10 > second >= 0:
                fin_sec = f"0{second}"
                break
        except:
            print("Please enter a number between 0 and 60.")
            continue
    
    global alarm_time
    alarm_time = f"{hour}:{fin_min}:{fin_sec}"
    
    
    
def alarm(set_alarm_timer):
    print("Your alarm has been set for:", set_alarm_timer)
    while True:
        time.sleep(1)
        c_time = datetime.datetime.now()
        current_time = c_time.strftime("%H:%M:%S")
        if current_time == set_alarm_timer:
            print("Time to wake up!")
            for i in range(3):
                winsound.PlaySound("Alarm03.wav", winsound.SND_FILENAME)
            break



get_time()
alarm(alarm_time)
