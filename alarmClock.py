from tkinter import *
from tkinter.ttk import *
import datetime
import time
from pygame import mixer
from threading import *


bg_col = "white"
col1 = "black"
col2 = "blue"
col3 = "purple"


window = Tk()
window.geometry("400x300")
window.title("ALARM CLOCK") 
window.configure(bg=bg_col)
s = Style(window)
s.configure("TFrame", font=('arial 18 bold'), background=bg_col)
s.configure("TLabel", font=('arial 18 bold'), background=bg_col)
# s.configure("TOptionMenu", width=2, font=('arial 15'))
s.configure("TButton", font=("Helvetica 15"))

frame_line = Frame(window, width=400, height=5, style="frame_line.TFrame")
s.configure("frame_line.TFrame", font=('arial 18 bold'), background=col2)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290)
frame_body.grid(row=1, column=0)

name = Label(frame_body, text="ALARM", style="name.TLabel")
s.configure("name.TLabel", font=('arial 18 bold'), background=bg_col, foreground=col3)
name.place(x=150, y=10)

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




def Threading():
    t1=Thread(target=alarm)
    t1.start()
    
def Stop_threading():
    mixer.music.stop
     
set_alarm = Button(frame_body, text="SET ALARM", command=Threading)
set_alarm.place(x=140, y=120)

stop_alarm = Button(frame_body, text="STOP ALARM", command=Stop_threading)
stop_alarm.place(x=135, y=160)
 
def sound_alarm():
    mixer.music.load("bless.mp3")
    mixer.music.play
    
    
def alarm():
    while True:
        set_alarm_time = f"{box_hour.get()}:{box_minute.get()}:{box_second.get()}"
 
        time.sleep(1)
 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        if current_time == set_alarm_time:
            mixer.init()
            sound_alarm()
 

window.mainloop()
