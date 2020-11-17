#importing necessary modules
import tkinter
from tkinter import *
import datetime
import time
import winsound

#creating a while loop
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time To Wake Up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get}"
    alarm(set_alarm_timer)


#initializing the tkinter window
clock = Tk()
clock.title("The_Tech_Thing Alarm Clock")
clock.geometry("450x250")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=110,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 250)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",12,"bold")).place(x=60, y=25)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=250,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=290,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=330,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time, font = ("Helvetica",10,"bold")).place(x =280,y=60)

#Execution of the window.
clock.mainloop()
