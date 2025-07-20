import customtkinter as ctk
import tkinter as tk
import pygame, sympy, numpy, random,sys,messagebox,csv,time,os
import numpy as np
from tkinter import *
from PIL import Image, ImageDraw , ImageTk
from sympy import *
music_paused = False
global timer_state , qnum , score_num
timer_state = 1 # set the timers state to 1 which means its active
score_num = 0
ctk.set_appearance_mode("light")
#Home Window
class Home(ctk.CTk): #Initialise a class for the main window.
    def __init__(self):
        super().__init__()
        self.difficulty_mode = Difficulty(self) #Create instance variable for Difficulty class so functions, variables from that can be accessed. 
        self.quiz = Quiz(self) #Create instance variable for Quiz class so functions, variables from that can be accessed. 
    def create_home(self): #This function is for setting up the main window. 
        self.title("Quavers Teaching Dillema")
        self.geometry("680x520")
        self.config(bg="#f7f4e4")
        self.resizable(False,False)
        self.iconbitmap("qd16x16_log1.ico")
        self.iconphoto(True,PhotoImage(file= 'qd16x16_logo1.png'))
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=0)
        self.grid_rowconfigure(2,weight=0)
        self.grid_rowconfigure(3,weight=0)
        self.grid_rowconfigure(4,weight=0)
        self.grid_rowconfigure(5,weight=0)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=0,minsize=300,uniform='a')
        self.my_img = ctk.CTkImage(Image.open("qd log1 fin3.png"),size=(283,215,Image.LANCZOS))
        self.img_label = ctk.CTkLabel(self,bg_color="#f7f4e4",text ='', image=self.my_img)
        self.img_label.grid(row=0, column =0,rowspan=2)
        self.myframe = ctk.CTkFrame(master=self)
    def widget_seperation(self): 
        img = Image.new("RGBA", (200, 500),(247, 244, 228,255))
        draw = ImageDraw.Draw(img)

        top = (100,0)
        bottom = (100,500)

        # Draw the 4 sides using lines
        draw.line([top, bottom], fill="black", width=10)        # Draw the line
        self.border = ctk.CTkImage(light_image=img, size=(200,500))
    def home_button_setup(self): #This function is for setting up all the widgets on the main window. 
        self.widget_seperation()
    def home_button_setup(self): #This function is for setting up all the widgets on the main window. 
        self.widget_seperation()
        self.border_lbl = ctk.CTkLabel(self,image=self.border, text = "" )
        self.border_lbl.grid(row=0,column=1,padx=(0,200),sticky='nsw',columnspan=1)
        self.username_lbl = ctk.CTkLabel(self, width=90,text="Username",font=('Calibri',16,'bold'))
        self.username_lbl.grid(row=0,column=(1),rowspan=1,padx=(0,200),pady=(50,0), sticky = "ne")
        self.username_entry = ctk.CTkEntry(self,width = 125,bg_color="#FFFFFF")
        self.username_entry.grid(row=0,column=1,columnspan=1,padx=(0,50),pady=(50,0),sticky='ne')
        self.age_lbl = ctk.CTkLabel(self, width=90,text="Age",font=('Calibri',16,'bold'))
        self.age_lbl.grid(row=0,column=1,rowspan=1,padx=(0,90),pady=(196,0), sticky = 'n')
        self.age_entry = ctk.CTkEntry(self,width = 125,bg_color="#FFFFFF")
        self.age_entry.grid(row=0,column=1,columnspan=1,padx=(200,0),pady=(0,75))
        self.difficulty_button = ctk.CTkButton(self, text="Choose Difficulty",width=140, command=self.create_difficulty_window)
        self.difficulty_button.grid(row=0, column=1,ipadx=10,ipady=10,padx=(0,75), pady=(0,90),rowspan=1,sticky='se')
        self.quiz_button = ctk.CTkButton(self, text="Start the Quiz!", command=self.create_quiz_window)
        self.quiz_button.grid(row=0, column=1,ipadx=10,ipady=10,rowspan=3,sticky='se',padx=(0,75))
    def kill_event(self,event):
            sys.exit(0)
    def create_difficulty_window(self): #Function made so that difficulty window can be accessed when the 'Difficulty' button is clicked. 
        print("Creating Difficulty Mode Window..")
        self.difficulty_mode.create_difficulty()
        self.difficulty_mode.diff_button_setup()
        print("..... > Difficulty Mode Window Created")
    def create_quiz_window(self):
        #if self.username_validity == 1:
        if self.difficulty_mode.difficulty_chosen == True:
            self.quiz.quiz_questions = self.difficulty_mode.quiz_questions
            self.quiz.create_questions_window()
            print("Loading Quiz Window...")
            #self.quiz.start_ques()
        elif self.difficulty_mode.difficulty_chosen == False:
            messagebox.showwarning("Warning", "You cannot start the quiz without selecting a difficulty")
        elif self.username_entry.get() == '':
            messagebox.showwarning("Info","Name must not contain numbers")


#Difficulty Mode Window
class Difficulty():
    def __init__(self,HomePage,):
        self.homepage = HomePage #Instance variable for the home window.
        self.difficulty_level = "" # Create a variable for the difficulty level, initialise it as empty string for now. 
        self.difficulty_chosen = False #This variable holds a boolean for checking if the difficulty mode has been chosen or not. 
        self.myquiz_filepath = "./Questions&Answers/" #Create a variable which stores the parentfile path for each csv file that holds the questions
        self.quiz_questions = [] #Initialise an empty list for the questions
        self.difficulty_modes = ['Easy','Medium','Hard','Extreme'] #I have created a list which stores each difficulty mode
        self.csvFiles_Names = ["Easy.csv","Medium.csv","Hard.csv","Extreme.csv"] #This is a list which stores the names of each csv file that uses the .csv extension . 
        #self.EasyFile = "./Questions&Answers/Easy.csv"
        #self.MediumFile = "./Questions&Answers/Medium.csv"
        #self.HardFile =  "./Questions&Answers/Hard.csv"
        #self.ExtremeFile =  "./Questions&Answers/Extreme.csv"

        #self.quiz_instance = Quiz()
    def create_difficulty(self): #Setup for difficulty window
        self.difficulty = Toplevel(self.homepage)
        self.difficulty.config(background="#000000")
        self.difficulty.title("Difficulty")
        self.difficulty.geometry("400x250")
        self.difficulty.grid_columnconfigure((0,3), weight=1)
        self.difficulty.grid_rowconfigure((0, 3), weight=0)
     # Button Setup for difficulty window
    def diff_button_setup(self): 

        self.difficulty_mode_colors = ['#11A800','#DDFF00','#820000',"#A161AF"]
        for index in range(len(self.difficulty_modes)):
            self.Buttons = ctk.CTkButton(self.difficulty, 
                                         text=self.difficulty_modes[index],
                                         font=("Segoe UI",16),
                                         fg_color=self.difficulty_mode_colors[index], 
                                         text_color="#000000",
                                         command=lambda i=index :self.read_difficulty_file(i)
                                         )
            self.Buttons.grid(pady=5)
    
    def read_difficulty_file(self,listIndex): 
        self.difficulty_chosen = True
        self.difficulty_level =  self.difficulty_modes[listIndex]
        myFile = self.myquiz_filepath + self.csvFiles_Names[listIndex]
        ##  self.read_Quiz()
        with open(myFile,"r") as file:
            for line_number , line_content in enumerate(file,0):
                self.quiz_questions.append(line_content)
        self.difficulty.destroy()

        #for i in self.quiz_questions: 
            #print(i)


#Quiz Window
class Quiz():
    def __init__(self,HomePage):
        self.homepage = HomePage #Create a variable that links to the home page
        self.qnum = -1 # I create a variable for keeping track of question number, this can be accessed anywhere inside of the class (function)
        self.quiz_questions = [] #Initialise an empty list for keeping track of the questions 
    #Function for creating the questions page
    def create_questions_window(self):
        #Global Variables for the class
        self.quiz = Toplevel(self.homepage)
        self.quiz.config(background="#f7f4e4")
        self.quiz.title("Questions") #Set the window title
        self.quiz.geometry("640x480") #Set the window size
        self.timer_setup()
        self.start_timer()
        self.score_setup()
        self.start_ques()
        self.show_next_question()
    def start_ques(self):
        self.q = ctk.CTkLabel(self.quiz,text="", text_color="#000000", font=("Segoe UI",10,"bold"))
        self.q.grid(row=4,column=3)
        self.q_statement = ctk.CTkLabel(self.quiz,text="w",text_color="#000000", font=("Segoe UI",10,"bold"))
        self.q_statement.grid(row=5,column=3)
        self.q_response = ctk.CTkEntry(self.quiz, font=("Segoe UI",16,"bold"))
        self.q_response.grid(row=6,column=3,columnspan=3,padx=20,pady=40)
        self.q_scoreb = ctk.CTkButton(self.quiz,text="Submit", font=("Segoe UI",18,"bold"),command=self.check_answer) 
        self.q_scoreb.grid(row=8,column =3,padx=20)
        self.img_label = ctk.CTkLabel(self.quiz,text='')
        self.img_label.grid(pady=10)

    def timer_setup(self): #Function for setting up the timer 
        self.timer = StringVar() #Initialise a string variable 
        self.timer.set("00:00:-01") #Set the string variable to be 00:00:-01 , when Start Quiz button is clicked, timer starts from 00:00:00
        self.tlabel = ctk.CTkLabel(self.quiz,textvariable=self.timer,text_color="#006AAC") #Create a label for the timer 
        self.tlabel.configure(font=("Segoe UI",18,"bold")) #Set the timer font
        self.tlabel.grid(row=1,column=3,sticky="e",padx=60) #Place the timer on the window 
    def start_timer(self):
        global timer_state
        if(timer_state==1): #Condition that depicts whether timer is active or not
            self.timepos = str(self.timer.get())
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
            self.timer.set(self.timepos)
            if timer_state == 1:
                self.quiz.after(930,self.start_timer)

            
    def score_setup(self):
        self.score = StringVar() #String Variable initialised to keep track of current score.
        self.score.set("0") #Set the value of this String Variable to 0.
        self.display_score = StringVar() #Create another String Variable for dynamic display and updates 
        self.display_score.set("Score: " + self.score.get()) #
        self.score.trace_add("write",self.update_score)
        self.quiz_scorelab = ctk.CTkLabel(self.quiz,textvariable=self.display_score,text_color="#006AAC")
        self.quiz_scorelab.configure(font=("Segoe UI",12,"bold"))
        self.quiz_scorelab.grid(row=3,column=3)
    
    def update_score(self,*args):
        self.display_score.set("Score: " + self.score.get())
   
    def score_increment(self):
        current_score = int(self.score.get())
        new_score = str(current_score + 1)
        self.score.set(new_score)
    
    def show_next_question(self):
        if self.qnum < len(self.quiz_questions):
            self.qnum = self.qnum + 1
            current = self.quiz_questions[self.qnum]

            # Show question
            row_content = current.split(",")
            question_type = row_content[0].strip()
            question_imgfile = row_content[1].strip()
            question_equation = row_content[2].strip()
            question_statement = row_content[4].strip()
            if question_type == 'i':
            # Show image
                    try:
                        temp = os.path.dirname(__file__)+question_imgfile
                        print(os.path.dirname(__file__)+question_imgfile)
                        absolute_path = '/Images/Easy/SquareArea_25.png,'
                        relative_path = os.path.relpath(absolute_path)
                        print(f"Relatice path from current directory: {relative_path}")
                        self.img_lod = ctk.CTkImage(Image.open(question_imgfile),size=(480,500,Image.LANCZOS))
                        self.img_label.configure(image=self.img_lod)
    # 2. Resize the PIL Image (not CTkImage!)
    # 3. Convert to CTkImage (size is optional here)
    # 4. Assign to label
                        #image_to_show = ImageTk.PhotoImage(image)
                        #self.picture.configure(image=image_to_show)
                        #self.picture.image = image_to_show
                    except FileNotFoundError:
                        self.img_label.configure(text="Image not found", image='')
                        print(os.path.dirname(__file__)+ f" {question_imgfile} ")

        else:
            messagebox.showinfo("Info","You have finished the quiz\n"f"You scored {self.score} / 10 ")   
        self.q.configure(text=f"Q{self.qnum + 1}: {question_equation}")
        self.q_statement.configure(text=f"{question_statement}")
        self.q_response.delete(0, tk.END)
        self.q_response.focus()

    def check_answer(self): #This function is used to check if the students input matches the correct or wrong answer to the question. 
        student_input = self.q_response.get().strip()
        print("Program collecting user input")
        #current = self.quiz_questions[self.qnum].split(",")[3]
        #current.split(",")[3]
        self.correct_ans = self.quiz_questions[self.qnum].split(",")[3]
        #validity = self.answer_validator(student_input)
        if student_input == self.correct_ans:
            self.score_increment()
            print("Score increased,correct answer")
            self.show_next_question()
            self.q_response.delete(0,END)
        else:
            print("Score did not increase,incorrect answer")
            self.show_next_question()

def main(): #Main Function
    home_page = Home()
    print("Opening Homepage...")
    home_page.create_home()
    home_page.bind("<Alt-q>",home_page.kill_event)
    home_page.bind("<Alt-d>",home_page.create_difficulty_window) #When the keybind Alt Q is detected, program will terminate, it refers to function kill_event()
    home_page.home_button_setup()
    home_page.mainloop()
main()