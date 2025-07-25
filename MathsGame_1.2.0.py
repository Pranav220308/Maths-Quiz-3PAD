"""
: maths4kids_1.1.0.py
Author: Pranav Kumar
Date: 2025/05/15
Version: 1.1.0
Description:
Interactive quiz program made with the tkinter library
for the purpose of mathematics practice for young children at a primary school age.
"""
#ver.1.1.0    
   #   - Special Letters (Symbols)
   #- Blank/No Input
   # - Boundaries
   # - Alphabet/letters

import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def validator(user_input):
    # Blanks
    if user_input == "":
        print("user input is blank")
        warning = Label(app, text="NO BLANKS!", fg="RED", font=("Comic Sans MS", 16))
        warning.place(relx=0.3, rely=0.1)

       
    # Alphabet, Whitespace, and Symbols
    elif user_input.isdigit() == False:
        if user_input.isalnum() == True:
            print("Alphabet detected")
            warning = Label(app, text="NO LETTERS!", fg="RED", font=("Comic Sans MS", 16))
            warning.place(relx=0.3, rely=0.1)
        elif " " in user_input:
            warning = Label(app, text="NO WHITESPACES!", fg="RED", font=("Comic Sans MS", 16))
            warning.place(relx=0.3, rely=0.1)
            print("Whitespace Detected")
        else:
            warning = Label(app, text="NO SYMBOLS!", fg="RED", font=("Comic Sans MS", 16))
            warning.place(relx=0.3, rely=0.1)
            print("Symbols Detected")    
    # Boundaries (user input is more than)
    elif len(user_input) > 6:
        print("Character Limit is 6")
    else:
        return True
    return False
def submt(user_entry):
    user_input = user_entry.get()
    validity = validator(user_input)
    if validity == True:
        if user_input == str(resultPLUS()):
            correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.3, rely=0.2)
        else:
            wrong = Label(app, text="Wrong!!!", fg="red", font=("Courier", 16))
            wrong.place(relx=0.3, rely=0.2)
    print("Checks Done")
    

def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    newQ = Label(
        app, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update

app = Tk()
app.title("Math Quiz")

app.geometry("250x300") # Set Window Size
app.resizable(False, False) # Do not allow for window resize

# Start button
start = Button(app, text="Start", command=try_again)
start.place(relx=0.45, rely=0.2)

# Entry text box
user_entry = Entry(app,font=("Comic Sans MS","16","bold"))
user_entry.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

# Code to submit answer
submit = Button(app, text="Submit", command=lambda: submt(user_entry))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

# Try again button
try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.39, rely=0.9)




app.mainloop()