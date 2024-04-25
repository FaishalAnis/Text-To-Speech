import _tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text To Speech")
root.geometry("900x700")
root.resizable(False, False)
root.configure(bg="#305065")

engine = pyttsx3.init()
def  speaknow():
    text = text_area.get(1.0, END)
    gender =gender_combobox.get()
    speed =speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()
    print()

# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=200)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="texts.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)
Label(Top_frame, text="Text To Speech", font="arial 50 bold", bg="white", fg="black").place(x=350, y=100)

#########
text_area=Text(root, font="Robote 20", bg="white", relief= GROOVE, wrap=WORD)
text_area.place(x=10,y=250, width=500, height=350)

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=560, y=250)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=740, y=250)

gender_combobox = Combobox(root, values=["Male", "Female"], font="arial 14", state='r', width=10)
gender_combobox.place(x=550,y=300)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=["Fast", "Normal", "Slow"], font="arial 14", state='r', width=10)
speed_combobox.place(x=730,y=300)
speed_combobox.set('Normal')

imageicon=PhotoImage(file="151840.png")
btn=Button(root,text="Speak",compound=LEFT, image=imageicon, width=156, height=60,font="arial 14 bold", command=speaknow)
btn.place(x=550,y=420)

imageicon2=PhotoImage(file="save.png")
btn=Button(root,text="Save",compound=LEFT, image=imageicon2, width=120, bg="#39c790", font="arial 14 bold", command=download)
btn.place(x=750,y=420)
root.mainloop()
