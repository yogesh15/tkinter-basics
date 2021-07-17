#import tkinter
from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label

#By including 'from tkinter import *' we can remove writting tkinter before tkinter class access. So the below line chanes to-
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#we can change Label by this two methods-
my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    my_label.config(text="I got clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()