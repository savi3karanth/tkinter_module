from tkinter import *

tkinter = Tk()
tkinter.title("My first GUI")
tkinter.minsize(width=500, height=400)

my_label = Label(text="I am Savitri", font=("Arial", 40, "normal"))
my_label.pack()

def button_got_clicked():
    new_text = input.get()
    my_label.config(text=new_text)  #If we give the input with any text and click me then the text will be printed in label
    #my_label.config(text="I got clicked")   # When the button is clicked the label will change to I got clicked


button = Button(text="Click me", command=button_got_clicked)
button.pack()

input = Entry(width=15)
input.pack()

tkinter.mainloop()