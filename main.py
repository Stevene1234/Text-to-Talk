from tkinter import *
from gtts import gTTS
from playsound import playsound
import os


root = Tk()
root.geometry("500x450")
root.configure(bg='ghost white')
root.title("You text, I'll talk!")




Msg = StringVar()
Label(root, text = "You text, I'll talk!", font = 'arial 15 bold', bg = 'white smoke').pack()
Label(root,text ='Enter Text', font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entryfield = Entry(root, textvariable = Msg ,width ='50')
entryfield.place(x=20,y=100)

def Text_to_talk():
#converts text to talk
    Message = entryfield.get()
    speech = gTTS(text = Message)
    speech.save('project.mp3')
    playsound('project.mp3')
    os.remove('project.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")


Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_talk ,width = '4', bg = 'lightgreen').place(x=25,y=140)
Button(root, text = 'Exit', font = 'arial 15 bold', width = '4' , command = Exit, bg = 'red').place(x=100 , y = 140)
Button(root, text = 'RESET',font = 'arial 15 bold', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()
