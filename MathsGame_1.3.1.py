"""
: maths4kids_1.1.0.py
Author: Pranav Kumar
Date: 2025/05/20
Version: 1.3.0
Description:
Interactive quiz program made with the tkinter library
for the purpose of mathematics practice for young children at a primary school age.
"""
#ver.1.1.0    
   #   - Special Letters (Symbols)
   #- Blank/No Input
   # - Boundaries
   # - Alphabet/letters

#ver 1.3.0
   #  - pop up windows 

import random , json
from tkinter import *
import tkinter as tk
from tkinter import messagebox

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def quit_quiz():
    response = messagebox.askyesno("Quit Quiz","Would you like to quit the quiz?")
    if response == 1: #If response variable is true then program will be terminated if the user selects "Yes" on the messagebox. 
        home_page.destroy()#Program is terminated/exited. 

def create_error_popups(error_message):
    error_popups = Toplevel(home_page) # Create new window
    error_popups.title("Warning") #set window title
    error_popups.geometry("200x150") #Setting window size
    error_popups.resizable(False, False) #Window size cannot be resized
    #messagebox.showwarning("Warning","NO BLANKS!!")
    error_popups_warning = Label(error_popups, text="", justify = "center", fg="RED", font=("Comic Sans MS", 16))
    error_popups_warning.config(text=error_message)
    error_popups_warning.place(relx=0.2, rely=0.3)
def validator(user_input):
    # Blanks
    if user_input == "":
        create_error_popups("NO BLANKS!")
        print("user input is blank")

       
    # Alphabet, Whitespace, and Symbols
    elif user_input.isdigit() == False:
        if user_input.isalnum() == True:
            print("Alphabet detected")
            create_error_popups("NO LETTERS!")
        elif " " in user_input:
            create_error_popups("NO WHITESPACES!")
            print("Whitespace Detected")
        else:
            create_error_popups("NO SYMBOLS")
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
            correct = Label(home_page, text="Correct!", fg="green", font=("Courier", 16))
            correct.place(relx=0.3, rely=0.2)
        else:
            wrong = Label(home_page, text="Wrong!!!", fg="red", font=("Courier", 16))
            wrong.place(relx=0.3, rely=0.2)
    print("Checks Done")
def save_data():
    correct = [
        {"Answer": f"{user_entry.get()}",
        "Username": "No Username"}
    ]
    

    json_object = json.dumps(correct, indent=2)
    
    with open("answers.json","a") as outfile:
        outfile.write(json_object)
    

def try_again():
    try_again.num1update = random.choice(num)
    try_again.num2update = random.choice(num)
    newQ = Label(
        home_page, text=f"{try_again.num1update}+{try_again.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    try_again
    return try_again.num1update + try_again.num2update

home_page = Tk()
home_page.title("Math Quiz")
home_page.config(background="#f7f4e4")
home_page.geometry("250x300") # Set Window Size
home_page.resizable(False, False) # Do not allow for window resize

# Start button
start = Button(home_page, text="Start",font=("Quicksand","10","bold"), command=try_again)
start.place(relx=0.45, rely=0.2)

# Entry text box
user_entry = Entry(home_page,font=("Comic Sans MS","16","bold"))
user_entry.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

# Code to submit answer
submit = Button(home_page, text="Submit", command=lambda: [submt(user_entry), save_data()])
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

#Quit button to exit program
quit_program = Button(home_page, text="Quit",bg="red",fg="white",command=quit_quiz)
quit_program.place(relx=0.85, rely=0.05)
# Try again button
try_again1 = Button(home_page, text="Try Again", command=try_again)
try_again1.config(command=lambda: [user_entry.delete(0,tk.END), try_again()])
try_again1.place(relx=0.39, rely=0.9)




home_page.mainloop()
