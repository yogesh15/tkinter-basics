#import tkinter
from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=40)

#Label
#By including 'from tkinter import *' we can remove writting tkinter before tkinter class access. So the below line chanes to-
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#New Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)


#Entry
input = Entry(width=15)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()