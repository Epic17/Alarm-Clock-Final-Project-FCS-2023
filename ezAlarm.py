import time
import datetime
import winsound
import pyaudio
from appJar import gui

p = pyaudio.PyAudio()
hourentry = " Hour  "
minuteentry = "Minute"
periodentry = "Period"


# This function enters the time into the "alarm" when the button is pressed
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        try:
            hr1 = app.getEntry(hourentry)
            min1 = app.getEntry(minuteentry)
        
            hr2 = round(hr1) # type: ignore
            min2 = round(min1) # type: ignore
               
            if 13 > hr2 > 0:
                global fin_hr
                fin_hr = hr2
                if 60 > min2 >= 0:
                    if 10 > min2:
                        global fin_min
                        fin_min = f"0{min2}"
                        period_check()
                    else:
                        fin_min = min2
                        period_check()
                else:
                    app.warningBox("Error", "Please enter a minute between 0 and 59.")
            else:
                app.warningBox("Error", "Please enter a hour between 1 and 12.")
        except TypeError:
            app.warningBox("Error", "Please enter a valid value.")

# This function makes sure the time is in the correct format
def period_check():
    am_pm1 = app.getOptionBox(periodentry)
    global fin_hr
    global fin_min
    
    if am_pm1 == "AM":
        if fin_hr == 12:
            fin_hr = "00"
            alarm_time = f"{fin_hr}:{fin_min}:00"
            alarm(alarm_time)
        elif 11 >= fin_hr >= 10:
            alarm_time = f"{fin_hr}:{fin_min}:00"
            alarm(alarm_time)
        elif 9 >= fin_hr:
            fin_hr = f"0{fin_hr}"
            alarm_time = f"{fin_hr}:{fin_min}:00"
            alarm(alarm_time)
    else:
        if 11 >= fin_hr:
            fin_hr += 12
            alarm_time = f"{fin_hr}:{fin_min}:00"
            alarm(alarm_time)
        else:
            alarm_time = f"{fin_hr}:{fin_min}:00"
            alarm(alarm_time)

# This function is used for the alarm. It sets an alarm and plays the alarm sound as well     
def alarm(set_alarm_timer):
    print("Your alarm has been set for:", set_alarm_timer)
    while True:
        time.sleep(1)
        c_time = datetime.datetime.now()
        current_time = c_time.strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
        if current_time == set_alarm_timer:
            print("Time to wake up!")
            try:
                for i in range(3):
                    winsound.PlaySound("AlarmSound.wav", winsound.SND_FILENAME)
            except:
                app.warningBox("Error", "Sound was unable to play. Please check your output device and try again.")
            break

# Creates the application GUI
app = gui("ezAlarm", "400x200")
app.addLabel("title", "Set your alarm below.")
app.setBg("lightblue")
app.setFont(18)
app.setLabelBg("title", "lightblue")
app.addLabelNumericEntry(hourentry)
app.addLabelNumericEntry(minuteentry)
app.addLabelOptionBox(periodentry, ["AM", "PM"])
app.addButtons(["Submit", "Cancel"], press)
app.setFocus(hourentry)
app.icon = "ezAlarm-icon.ico"

# Checks for an output device. If found, continue with app startup.
# If not, cancel app startup and prompt user to connect an output device.
try:
    p.get_default_output_device_info()
    app.go()
except IOError:
    app.warningBox("Error", "No output device found. Please check your output device and try again.")