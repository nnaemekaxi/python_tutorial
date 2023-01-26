from tkinter import *
from tkinter.ttk import *
import datetime
import time
# from pygame import mixer
import winsound
# from playsound import playsound
from threading import *

# Colors for the interface
bg_col = "white"
col1 = "black"
col2 = "blue"
col3 = "purple"

# Tkinter method is assigned the variable window
window = Tk()
window.geometry("400x300")
window.title("ALARM CLOCK") 
window.configure(bg=bg_col)

# Style method is introduced as this is the best way to style tkinter.ttk interfaces
# It allows different elements to be configured globally, which can be modified later in local elements
s = Style(window)
s.configure("TFrame", font=('arial 18 bold'), background=bg_col)
s.configure("TLabel", font=('arial 18 bold'), background=bg_col)
# s.configure("TOptionMenu", width=2, font=('arial 15'))
s.configure("TButton", font=("Helvetica 15"))

# This creates a line to separate the interface head and body
frame_line = Frame(window, width=400, height=5, style="frame_line.TFrame")
s.configure("frame_line.TFrame", font=('arial 18 bold'), background=col2)
frame_line.grid(row=0, column=0)

# This creates the main body of the alarm clock
frame_body = Frame(window, width=400, height=290)
frame_body.grid(row=1, column=0)

# This gives a title to the body of the alarm clock
name = Label(frame_body, text="ALARM", style="name.TLabel")
s.configure("name.TLabel", font=('arial 18 bold'), background=bg_col, foreground=col3)
name.place(x=150, y=10)

# This gives a title to the hour section/the options box for hour
hour = Label(frame_body, text="H")
hour.place(x=130, y=50)
box_hour = Combobox(frame_body, width=2, font=('arial 15'))
box_hour['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
box_hour.current(0)
box_hour.place(x=130, y=80)
# hour = StringVar(window)
# hour.set(box_hour)
# hrs = OptionMenu(frame_body, hour, *box_hour)
# hrs.place(x=130, y=80)

# This gives a title to the minutes section/the options box for minutes
minute = Label(frame_body, text="M")
minute.place(x=180, y=50)
box_minute = Combobox(frame_body, width=2, font=('arial 15'))
box_minute['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
box_minute.current(0)
box_minute.place(x=180, y=80)
# minute = StringVar(window)
# minute.set(box_minute)
# minutes = OptionMenu(frame_body, minute, *box_minute)
# minutes.place(x=180, y=80)


# This gives a title to the seconds section/the options box for seconds
second = Label(frame_body, text="S")
second.place(x=230, y=50)
box_second = Combobox(frame_body, width=2, font=('arial 15'))
box_second['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
box_second.current(0)
box_second.place(x=230, y=80)
# second = StringVar(window)
# second.set(box_second)
# seconds = OptionMenu(frame_body, second, *box_second)
# seconds.place(x=230, y=80)



# This function sets off/triggers the alarm once the conditions set in the alarm are met
def Threading():
    t1=Thread(target=alarm)
    t1.start()
    
# def Stop_threading():
#     mixer.music.stop

#  This is the button for activating the selected inputs for the alarm clock
set_alarm = Button(frame_body, text="SET ALARM", command=Threading)
set_alarm.place(x=140, y=120)

# stop_alarm = Button(frame_body, text="STOP ALARM", command=Stop_threading)
# stop_alarm.place(x=135, y=160)
 
# def sound_alarm():
#     mixer.music.load("bless.mp3")
#     mixer.music.play
    
# This defines behaviour of the alarm clock once triggered 
def alarm():
    while True:
        # The hour, minute and seconds values are assigned a variable
        set_alarm_time = f"{box_hour.get()}:{box_minute.get()}:{box_second.get()}"
 
        time.sleep(1)

        # It extracts the current time from the device
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # It checks if the current_time is the same as the set_alarm_time. If true, it plays the alarm song
        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            # playsound("bless.mp3")
            # mixer.init()
            # sound_alarm()
            
# The method that houses all the functionality placed inside Tkinter interface. Without it, the interface goes blank
window.mainloop()
