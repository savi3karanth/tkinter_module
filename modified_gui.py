import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label.config(text=new_text)

window = Tk() # we use this same like screen on turtle
window.title("My first GUI program")
window.minsize(width=300, height=200)
window.config(padx=100, pady=200) # Padding around the table means giving more space around

# Label is a class which we use here
label = Label(text="I am a Label", font=("Arial", 24, "italic"))
# to run the above line we need to write this line if not no text will be displayed
#label.pack() when you write grid we need to comment the pack
label["text"] = "New text"
label.config(text="New text")
label.place(x=100, y=200)
label.grid(column=0, row=0)
label.config(padx=50, pady=50)


#button
button = Button(text="Click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

#new_button
new_botton = Button(text="New button")
new_botton.grid(column=2, row=0)


#input
input = Entry(width=10)
#input.pack()
print(input.get())
input.grid(column=3, row=2)

tkinter.mainloop()
