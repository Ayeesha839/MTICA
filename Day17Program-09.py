#message widge:used to display short text
#fonts can be changed,text may span more than one line

from tkinter import *
master=Tk()
demo_text="This is a sample demo of message widget."
msg=Message(master,text=demo_text)
msg.config(bg='lightgreen',font=('times',24,'italic'))
msg.pack()

