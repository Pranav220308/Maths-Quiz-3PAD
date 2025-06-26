import customtkinter as ctk
import tkinter as tk
import pygame, sympy, numpy, random,sys,messagebox
import numpy as np
from tkinter import *
from PIL import *
from sympy import *
'''Version 2.2
-  Questions Class
-  Improvised Music Player
-  Main function '''
#Global Variables
music_paused = False
global timer_state , qnum , score_num
timer_state = 1 # set the timers state to 1 which means its active
qnum=0 #Global Variable for Question Number
score_num = 0 # Global Variable for Score Number

#Set the theme
ctk.set_appearance_mode("light") #set the theme of the program to light mode.
pygame.mixer.init() # Initialise the pygame mixer for playing streamed music
#Questions Window
class Questions():
    def __init__(self,HomePage):
        self.homepage = HomePage #Create a variable that links to the home page
    #Function for creating the questions page
    def create_questions_window(self):
        #Global Variables for the class
        self.questions = Toplevel(self.homepage) 
        self.questions.config(background="#f7f4e4")
        self.questions.title("Questions") #Set the window title
        self.questions.geometry("640x480") #Set the window size
        self.questions.lift()
        self.questions.grid_columnconfigure((0,6), weight=0) # Column configurations for this window 
        self.questions.grid_rowconfigure((0, 6), weight=0) # Row configurations
        self.timer_setup() # Function for setting up the timer 
        self.start_timer() # Function for starting the timer
        self.questions_text = ctk.CTkLabel(self.questions,text="", font=("Segoe UI",10,"bold"))
    def start_ques(self):
        self.questions_blank_response = ctk.CTkEntry(self.questions, font=("Segoe UI",16,"bold"))
        self.questions_blank_response.grid(row=5,column=1,padx=20,pady=40)
    
    def timer_setup(self): #Function for setting up the timer 
        self.questions_timer = StringVar() #Initialise a string variable 
        self.questions_timer.set("00:00:-01") #Set the string variable to be 00:00:-01 , when Start Quiz button is clicked, timer starts from 00:00:00
        self.questions_tlabel = ctk.CTkLabel(self.questions,textvariable=self.questions_timer,text_color="#006AAC") #Create a label for the timer 
        self.questions_tlabel.configure(font=("Segoe UI",18,"bold")) #Set the timer font
        self.questions_tlabel.grid(row=1,column=3,sticky="e",padx=40) #Place the timer on the window 

    def start_timer(self):
        global timer_state
        if(timer_state==1): #Condition that depicts whether timer is active or not
            self.timepos = str(self.questions_timer.get())
            hours,minutes,seconds = map(int,self.timepos.split(":")) #Iterate through the textvariable and format as list
            hours = int(hours) #Convert the string variable for hours to a integer
            minutes = int(minutes) #Convert the string variable for minutes to a integer
            seconds = int(seconds) #Convert the string variable for seconds to a integer
            if seconds < 59: # The program checks if the 'seconds' part of the timer is less than 59
                seconds+=1 # Add 1 if the seconds in the timer is less than 59
            elif seconds == 59: # Program checks if the seconds part of the timer is at 59 seconds
                seconds = 0 # Program resets the seconds to 0 once it has passed 59
                if minutes < 59: # The program checks if the 'minutes' part of the timer is less than 59
                    minutes+=1 #Add 1 if the minutes in the timer is less than 59 to keep the minutes incrementing
                elif minutes == 59: # Program checks if the minutes part of the timer is at 59 minutes 
                    hours +=1 # Add 1 to the hours part of the timer if it is above 59 minutes.
            if hours < 10: #Program checks if the hours variable is less than 10 according to the timers position 
                hours = str(0) + str(hours)
            else:
                hours = str(hours) # Convert the hours variable back to a string 
            if minutes < 10:   #Program checks if the minutes variable is less than 10 according to the timers position 
                minutes = str(0) + str(minutes) # Program will 
            else:
                minutes = str(minutes) # Convert the minutes variable back to a string 
            if seconds < 10:
               seconds = str(0) + str(seconds)
            else:
                seconds=str(seconds)
            self.timepos = hours+":"+minutes+":"+seconds
            self.questions_timer.set(self.timepos)
            if timer_state == 1:
                self.questions.after(930,self.start_timer)
#Difficulty Selection
class Difficulty():
    def __init__(self,HomePage):
        self.homepage = HomePage #Store the parent window to a variable
    def create_difficulty(self,event):
        self.difficulty = Toplevel(self.homepage)
        self.difficulty.config(background="#000000")
        self.difficulty.title("Difficulty")
        self.difficulty.geometry("400x250")
        self.difficulty.grid_columnconfigure((0,3), weight=1)
        self.difficulty.grid_rowconfigure((0, 3), weight=0)
    # Temporary Button Setup for difficulty window
    def diff_button_setup(self,event):
        self.difficulty_Easy = ctk.CTkButton(self.difficulty,fg_color="#11A800",  text="😄 Easy", font=("Segoe UI",16),text_color="#FFFFFF",command=self.close_difficulty_window)
        self.difficulty_Easy.grid(row=0,column=2,padx=10,pady=10,sticky='nsew')
        self.difficulty_Normal = ctk.CTkButton(self.difficulty,fg_color="#DDFF00", text="😐 Normal",font=("Segoe UI",16),text_color="#000000",)
        self.difficulty_Normal.grid(row=1,column=2,padx=10,pady=10,sticky="nsew")
        self.difficulty_Hard = ctk.CTkButton(self.difficulty,fg_color="#820000" ,text="😠 Hard",font=("Segoe UI",16),text_color="#FFFFFF")
        self.difficulty_Hard.grid(row=2,column=2,padx=10,pady=10,sticky="nsew")
        self.difficulty_Extreme = ctk.CTkButton(self.difficulty,fg_color="#470057" ,text="😈 Extreme",font=("Segoe UI",16),text_color="#FFFFFF")
        self.difficulty_Extreme.grid(row=3,column=2,padx=10,pady=10,sticky="nsew")
    
    def close_difficulty_window(self):
            messagebox.showinfo("Difficulty Selected",f"Difficulty Selected: {self.difficulty_Easy._text}")
            print("Selected Difficulty:",self.difficulty_Easy._text)
            self.difficulty.destroy()

#Home Window
class Home(ctk.CTk):
    def __init__(self):
        super().__init__() 

    def create_home(self):
        self.title("Quavers Teaching Dillema")
        self.geometry("640x480")
        self.config(bg="#f7f4e4")
        self.resizable(False,False)
        self.p1 = tk.PhotoImage(file= 'qd16x16_logo1.png')
        self.iconphoto(False,self.p1)

        self.grid_columnconfigure((0,10), weight=1)
        self.grid_rowconfigure((0, 10),weight=1)
        self.my_img = ctk.CTkImage(Image.open("qd log1 fin3.png"),size=(380,285))
        self.img_label = ctk.CTkLabel(self,bg_color="#f7f4e4",text ='', image=self.my_img)
        self.img_label.grid(row=0, column =0)
    def home_button_setup(self):
        self.username_entry = ctk.CTkLabel(self, text="Username")
        self.username_entry.grid(row=1,column=0)
        self.entry = ctk.CTkEntry(self,width = 150)
        self.entry.grid(row=2,column=0)
        self.difficulty_button = ctk.CTkButton(self, text="Difficulty", command=self.create_difficulty_window)
        self.difficulty_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.questions_button = ctk.CTkButton(self, text="Start Quiz", command=self.create_question_window)
        self.questions_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.button1 = ctk.CTkButton(self, text="PLAY Music", command=self.play_music_player)
        self.button1.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        self.button2 = ctk.CTkButton(self, text="STOP Music", command=self.paused_music_player)
        self.button2.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        radio_var = ctk.IntVar(value=0)
        self.radiobutton_1 = ctk.CTkRadioButton(self, text="Easy",variable=radio_var,value = 1)
        self.radiobutton_1.grid(row=0,column=3)
        self.radiobutton_2 = ctk.CTkRadioButton(self, text="Normal",variable=radio_var,value = 2)
        self.radiobutton_2.grid(row=1,column=3, columnspan=3)
        self.radiobutton_2 = ctk.CTkRadioButton(self, text="Hard",variable=radio_var,value = 3)
        self.radiobutton_2.grid(row=2,column=3,columnspan=3)
    def kill_event(self,event):
            sys.exit(0)
        
        
    #Difficulty Window Creation
    def create_difficulty_window(self,event=None):
        print("Window Creating...")
        difficulty_window = Difficulty(self)
        difficulty_window.create_difficulty(event)
        print("Window Created")
        difficulty_window.diff_button_setup(event)
    def create_question_window(self):
        questions_window = Questions(self)
        questions_window.create_questions_window()
        questions_window.start_ques()
        print("Loading Questions Window...")

    #Music Player
    def play_music_player(self):
            global music_paused
            if music_paused:
                pygame.mixer.music.unpause()
                music_paused = False
                print("Resumed Music")
            elif not pygame.mixer.music.get_busy() or pygame.mixer.music.get_pos==-1:
                pygame.mixer.music.load("My Innermost Apocalypse.flac")
                pygame.mixer.music.play(loops=1)
                music_paused = False
                print("Music playing")
    def paused_music_player(self):
        global music_paused
        music_paused = False
        if pygame.mixer.music.get_busy(): # Check if music is currently playing
            pygame.mixer.music.pause()
            music_paused = True
            print("Paused Music")
        elif music_paused: # If music_paused is True, it means it was previously paused
            pygame.mixer.music.unpause()
            music_paused = False

def main(): #Main Function
    home_page = Home()
    print("Opening Homepage...")
    home_page.create_home()
    home_page.bind("<Alt-q>",home_page.kill_event)
    home_page.bind("<Alt-d>",home_page.create_difficulty_window) #When the keybind Alt Q is detected, program will terminate, it refers to function kill_event()
    home_page.home_button_setup()
    home_page.mainloop()
main()

