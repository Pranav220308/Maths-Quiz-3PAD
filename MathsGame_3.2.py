import customtkinter as ctk
import tkinter as tk
import random,sys,csv,time,os,warnings,json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageDraw , ImageTk
music_paused = False
global timer_state, qnum, score_num
timer_state = 1  # The timer has 2 states , if timer_state is set to 1 the timer is active, if it is 0 the timer is stopped.
score_num = 0
ctk.set_appearance_mode("light")
ctk.set_default_color_theme(
    'Component Trialling/Program Theme/Theme 3/theme3.json')
# Home Window


class Home(ctk.CTk):  # Initialise a class for the main window.
    def __init__(self, difficulty_inst, quiz_inst, leaderboard_inst):
        super().__init__()
        self.difficulty_mode = difficulty_inst #Store instance variables of the difficulty class so that attributes from it can be accessed here
        self.quiz = quiz_inst
        self.leaderboard = leaderboard_inst
        # self.difficulty_mode = Difficulty(self) #Create instance variable for Difficulty class so functions, variables from that can be accessed.
        # self.quiz = Quiz(self) #Create instance variable for Quiz class so functions and variables from that can be accessed.
        undo_stack = []
        redo_stack = []

    def create_home(self):  # This function is for setting up the main window.
        self.title("Quavers Teaching Dillema")
        self.geometry("680x520")
        self.config(bg="#b4cbed")
        self.resizable(False, False)
        self.iconbitmap("qd16x16_log1.ico")
        self.iconphoto(True, PhotoImage(file='qd16x16_logo1.png'))
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0, minsize=300, uniform='a')
        self.my_img = ctk.CTkImage(Image.open(
            "QDLogo3_transp.png"), size=(300, 300, Image.LANCZOS))
        self.img_label = ctk.CTkLabel(
            self, bg_color="#9dbbe7", text='', image=self.my_img)
        self.img_label.grid(row=0, column=0, sticky='w')
        self.myframe = ctk.CTkFrame(master=self)

    def widget_seperation(self):
        img = Image.new("RGBA", (200, 500), (180, 203, 237, 255))
        draw = ImageDraw.Draw(img)

        top = (100, 0)
        bottom = (100, 500)

        # Draw the 4 sides using lines
        draw.line([top, bottom], fill="black", width=10)        # Draw the line
        self.border = ctk.CTkImage(light_image=img, size=(200, 500))

    # This function is for setting up all the widgets on the main window.
    def home_button_setup(self):
        self.widget_seperation()
        self.border_lbl = ctk.CTkLabel(self,image=self.border, text = "" )
        self.border_lbl.grid(row=0,column=1,padx=(0,200),pady=(10,0),sticky='nsew',columnspan=1,rowspan=1)
        self.username_lbl = ctk.CTkLabel(self, width=90,text="Username",font=("Lexend",14,'bold'),bg_color="#9dbbe7")
        self.username_lbl.grid(row=0,column=(1),rowspan=1,padx=(0,200),pady=(50,0), sticky = "ne")
        self.username_entry = ctk.CTkEntry(self,width = 130,bg_color="#b4cbed",font=("Lexend",14,'bold'))
        self.username_entry.grid(row=0,column=1,columnspan=1,padx=(0,50),pady=(50,0),sticky='ne')
        self.qamount_lbl = ctk.CTkLabel(self, width=90,text="Question Amount",font=("Lexend",14,'bold'),bg_color="#9dbbe7")
        self.qamount_lbl.grid(row=0,column=1,rowspan=1,padx=(0,50),pady=(196,0), sticky = 'n')
        self.qamount_selector = ctk.CTkComboBox(self,values=['3','10','15'],font=("Lexend",14,"bold"),bg_color="#b4cbed",state='readonly')
        self.qamount_selector.set("")
        self.qamount_selector.grid(row=0,column=1,columnspan=1,padx=(0,20),pady=(0,90),sticky='e')
        self.leaderboard_button = ctk.CTkButton(self, text="Leaderboard",font=("Lexend",14,'bold'),width=140,bg_color="#b4cbed",command = self.leaderboard.create_leaderboard_window)
        self.leaderboard_button.grid(row=0, column=1,ipadx=10,ipady=10,padx=(0,75), pady=(0,160),rowspan=1,sticky='se')
        self.difficulty_button = ctk.CTkButton(self, text="Choose Difficulty",font=("Lexend",14,'bold'),width=140,bg_color="#b4cbed", command=self.create_difficulty_window)
        self.difficulty_button.grid(row=0, column=1,ipadx=10,ipady=10,padx=(0,75), pady=(0,80),rowspan=1,sticky='se')
        self.quiz_button = ctk.CTkButton(self, text="Start the Quiz!",font=("Lexend",14,'bold'),bg_color="#b4cbed", command=self.create_quiz_window)
        self.quiz_button.grid(row=0, column=1,ipadx=10,ipady=10,rowspan=3,sticky='se',padx=(0,75))
        self.about = ctk.CTkButton(self, text="About",font=("Lexend",14,'bold'),bg_color="#b4cbed")
        self.about.grid(row=0,column=0,sticky='sw',ipady=10,ipadx=10,padx=(70,0))

    def kill_event(self, event):
        sys.exit(0)
    def clear_widgets(self):
        for widget in self.winfo_children():
            if isinstance(widget,ctk.CTkEntry):
                widget.delete(0,END)
            elif isinstance(widget,ctk.CTkComboBox):
                widget.set("")
    def reset_game_state_quiz(self):
        global timer_state, score_num
        timer_state = 1
        score_num = 0
        self.difficulty_mode.difficulty_chosen = False
        self.difficulty_mode.quiz_questions = []
        self.quiz.quiz_questions = []
        self.quiz.qnum_current = -1
        self.clear_widgets()

    def reset_game_state_home(self):
        global timer_state, score_num
        timer_state = 1
        score_num = 0
        self.difficulty_mode.difficulty_chosen = False
        self.difficulty_mode.quiz_questions = []
        self.quiz.quiz_questions = []
        self.quiz.qnum_current = -1

    # Function made so that difficulty window can be accessed when the 'Difficulty' button is clicked.
    def create_difficulty_window(self):
        print("Creating Difficulty Mode Window..")
        self.difficulty_mode.create_difficulty()
        self.difficulty_mode.diff_button_setup()
        print("..... > Difficulty Mode Window Created")

    def create_quiz_window(self):
        # if self.username_validity == 1:
        if self.username_validator() == True:
            if len(self.qamount_selector.get()) != 0:
                if self.difficulty_mode.difficulty_chosen == True:
                    self.store_user_details()
                    self.stored_username = self.username_input
                    self.stored_qamount  = self.qamount_selector.get()
                    self.quiz.quiz_questions = self.difficulty_mode.quiz_questions
                    self.clear_widgets()
                    self.withdraw()
                    self.quiz.create_questions_window()
                    print("Loading Quiz Window...")
                elif self.difficulty_mode.difficulty_chosen == False:
                    messagebox.showwarning(
                        "Warning", "You cannot start the quiz without selecting a difficulty")
            else:
                messagebox.showwarning(
                    "Warning", "You cannot start the quiz without selecting how many questions")

    # Function used to check for certain cases in the username input.
    def username_validator(self):
        self.username_input = str(self.username_entry.get().strip())
        if len(self.username_input) == 0:
            messagebox.showwarning("Warning", "Name must not be left blank")
            return False
        # Iterate through each character in the username input and check if there are characters which are not alphabetical.
        elif not any(char.isalpha() for char in self.username_input):
            messagebox.showwarning(
                "Warning", "Username must contain at least one letter.\nProgram will not accept inputs that contain only numbers and symbols.")
            return False
        elif " " in self.username_input:
            messagebox.showwarning(
                "Warning", "There should be no whitespaces in the username..\nProgram will remove the whitespaces found.")
            self.username_entry.delete(0, END)
            self.username_entry.insert(0, self.username_input.replace(" ", ""))
            # print("whitespaces")
            return False
        elif len(self.username_input) > 12:
            messagebox.showwarning(
                "Warning", "Username cannot be above 12 characters.\nIt has been shortened to 12 characters now.")
            self.username_entry.delete(0, END)
            self.username_entry.insert(0, self.username_input[:12])
            return False
        elif len(self.username_input) < 4:
            messagebox.showwarning(
                "Warning", "Username cannot be less than 4 characters ")
            return False
        else:
            print("valid name")
            return True

    # This function is for storing the user details.
    def store_user_details(self):
        # Store the filename of the users details to a variable.
        f_path = "user_details.json"
        # Create a blank list for the users details, certain criteria is appended later.
        user_details = []
        print("init list for storing user details")
        user_details.append([self.username_input, self.qamount_selector.get(
        ), self.difficulty_mode.difficulty_level])
        try:
            with open(f_path, 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = []

        user_data.append(user_details)

        with open(f_path, 'w') as file:
            json.dump(user_data, file, indent=4)

    def undo_username():  # WIP
        print("")

# Difficulty Mode Window


class Difficulty():
    def __init__(self, quiz_inst, leaderboard_inst, home_inst):
        self.quiz = quiz_inst
        self.leaderboard = leaderboard_inst
        self.homepage = home_inst  # Instance variable for the home window.
        # Create a variable for the difficulty level, initialise it as empty string for now.
        self.difficulty_level = ""
        # This variable holds a boolean for checking if the difficulty mode has been chosen or not.
        self.difficulty_chosen = False
        # Create a variable which stores the parentfile path for each csv file that holds the questions.
        self.myquiz_filepath = "./Questions&Answers/"
        self.quiz_questions = []  # Initialise an empty list for the questions.
        # I have created a list which stores each difficulty mode.
        self.difficulty_modes = ['Easy', 'Medium', 'Hard', 'Extreme']
        # This is a list which stores the names of each csv file that uses the .csv extension .
        self.csvFiles_Names = ["Easy.csv",
                               "Medium.csv", "Hard.csv", "Extreme.csv"]

    def create_difficulty(self):  # Setup for difficulty window
        self.difficulty = Toplevel(self.homepage)
        self.difficulty.config(background="#000000")
        self.difficulty.title("Difficulty")
        self.difficulty.geometry("400x250")
        self.difficulty.grid_columnconfigure((0, 3), weight=1)
        self.difficulty.grid_rowconfigure((0, 3), weight=0)
     # Button Setup for difficulty window

    def diff_button_setup(self):

        self.difficulty_mode_colors = [
            '#11A800', '#DDFF00', '#820000', "#A161AF"]
        for entry in range(len(self.difficulty_modes)):
            self.Buttons = ctk.CTkButton(self.difficulty,
                                         text=self.difficulty_modes[entry],
                                         font=("Lexend", 16),
                                         fg_color=self.difficulty_mode_colors[entry],
                                         text_color="#000000",
                                         command=lambda i=entry: self.read_difficulty_file(i))
            self.Buttons.grid(pady=10, padx=(50, 0))

    def read_difficulty_file(self, listIndex):
        # Here we are storing the condition that the user has chosen a difficulty and is true.
        self.difficulty_chosen = True
        self.difficulty_level = self.difficulty_modes[listIndex]
        myFile = self.myquiz_filepath + self.csvFiles_Names[listIndex]
        # Program initiates a blank list for all content related to the questions
        self.quiz_questions = []
        with open(myFile, "r", encoding='utf-8') as file:
            for line_number, line_content in enumerate(file, 0):
                # We append all content per row inside of the csvfiles to this blank list.
                self.quiz_questions.append(line_content)
        # Shuffle the questions around to provide more playability.
        random.shuffle(self.quiz_questions)
        selected_amount = int(self.homepage.qamount_selector.get())
        self.quiz_questions = self.quiz_questions[:selected_amount]
        print(
            f"Loaded {len(self.quiz_questions)} questions for {self.difficulty_level}")
        self.difficulty.destroy()

        # for i in self.quiz_questions:
        # print(i)


# Quiz Window
class Quiz():
    def __init__(self, difficulty_inst, leaderboard_inst, home_inst):
        # Class instance variables
        self.difficulty = difficulty_inst
        self.leaderboard = leaderboard_inst
        self.homepage = home_inst  # Create a variable that links to the home page
        # I create a variable for keeping track of question number, this can be accessed anywhere inside of the class (function)
        self.qnum_current = -1
        # self.qnum_total = self.quiz.qamount_selector.get()
        self.quiz_questions = []  # Initialise an empty list for keeping track of the questions
        self.messagebox_open = False
    # Function for creating the questions page

    def create_questions_window(self):
        # Global Variables for the class
        self.quiz = Toplevel(self.homepage)
        self.quiz.protocol("WM_DELETE_WINDOW", self.return_home_quiz)
        self.quiz.config(bg="#b4cbed")
        self.quiz.title("Questions")  # Set the window title
        self.quiz.geometry("680x520")  # Set the window size
        self.timer_setup()
        global timer_state
        timer_state = 1
        self.timer_init()
        self.score_setup()
        self.start_ques()
        self.show_next_question()

    def start_ques(self):
        print(f"Question Amount: {self.homepage.stored_qamount}")
        self.q = ctk.CTkLabel(
            self.quiz, text="", text_color="#000000", font=("Lexend", 16, "bold"))
        self.q.grid(row=4, column=3)
        self.q_statement = ctk.CTkLabel(
            self.quiz, text="w", text_color="#000000", font=("Lexend", 16, "bold"))
        self.q_statement.grid(row=5, column=3)
        self.q_response = ctk.CTkEntry(self.quiz, font=("Lexend", 14, "bold"))
        self.q_response.grid(row=6, column=3, columnspan=3, padx=20, pady=40)
        self.q_submit = ctk.CTkButton(self.quiz, text="Submit", font=(
            "Lexend", 18, "bold"), command=self.check_answer)
        self.q_submit.grid(row=8, column=3, padx=20)
        self.quiz.bind("<Return>",lambda event: self.check_answer())
        self.img_label = ctk.CTkLabel(self.quiz, text='')
        self.img_label.grid(pady=10)

    def timer_setup(self):  # Function for setting up the timer
        self.timer = StringVar()  # Initialise a string variable
        # Set the string variable to be 00:00:00 , when Start Quiz button is clicked, timer starts counting upwards from 00:00:00
        self.timer.set("00:00:00")
        # Create a label for the timer
        self.tlabel = ctk.CTkLabel(
            self.quiz, textvariable=self.timer, text_color="#006AAC")
        self.tlabel.configure(font=("Lexend", 18, "bold")
                              )  # Set the timer font
        # Place the timer on the window
        self.tlabel.grid(row=1, column=3, sticky="ew", padx=60)
    
    def stop_timer(self):
        global timer_state
        timer_state = 0
    def start_time(self):
        global timer_state
        timer_state = 1
        self.active_timer()
    def active_timer(self):
        global count
        self.timer_init()

    def timer_init(self):
        global timer_state
        if timer_state == 1:  # Condition that depicts whether timer is active or not
            self.timepos = str(self.timer.get())
            # Iterate through the textvariable and format as list
            hours, minutes, seconds = map(int, self.timepos.split(":"))
            # Convert the string variable for hours to a integer
            hours = int(hours)
            # Convert the string variable for minutes to a integer
            minutes = int(minutes)
            # Convert the string variable for seconds to a integer
            seconds = int(seconds)
            if seconds < 59:  # The program checks if the 'seconds' part of the timer is less than 59
                seconds += 1  # Add 1 if the seconds in the timer is less than 59
            elif seconds == 59:  # Program checks if the seconds part of the timer is at 59 seconds
                seconds = 0  # Program resets the seconds to 0 once it has passed 59
                if minutes < 59:  # The program checks if the 'minutes' part of the timer is less than 59
                    minutes += 1  # Add 1 if the minutes in the timer is less than 59 to keep the minutes incrementing
                elif minutes == 59:  # Program checks if the minutes part of the timer is at 59 minutes
                    # Add 1 to the hours part of the timer if it is above 59 minutes.
                    hours += 1
            if hours < 10:  # Program checks if the hours variable is less than 10 according to the timers position
                hours = str(0) + str(hours)
            else:
                # Convert the hours variable back to a string
                hours = str(hours)
            if minutes < 10:  # Program checks if the minutes variable is less than 10 according to the timers position
                minutes = str(0) + str(minutes)  # Program will
            else:
                # Convert the minutes variable back to a string
                minutes = str(minutes)
            if seconds < 10:
                seconds = str(0) + str(seconds)
            else:
                seconds = str(seconds)
            self.timepos = hours+":"+minutes+":"+seconds
            self.timer.set(self.timepos)
            if timer_state == 1:
                self.quiz.after(930, self.active_timer)

    # This function is for setting up the score counter.
    def score_setup(self):
        # String Variable initialised to keep track of current score.
        self.score = StringVar()
        self.score.set("0")  # Set the value of this String Variable to 0.
        # Create another String Variable for dynamic display and updates
        self.display_score = StringVar()
        self.display_score.set("Score: " + self.score.get())
        self.score.trace_add("write", self.update_score)
        self.quiz_scorelab = ctk.CTkLabel(
            self.quiz, textvariable=self.display_score, text_color="#006AAC")
        self.quiz_scorelab.configure(font=("Lexend", 12, "bold"))
        self.quiz_scorelab.grid(row=3, column=3)

    def update_score(self, *args):
        self.display_score.set("Score: " + self.score.get())

    def score_increment(self):
        current_score = int(self.score.get())
        new_score = str(current_score + 1)
        self.score.set(new_score)

    def shuffle_questions(self):
        print("")

    def show_next_question(self):
        self.qnum_current = self.qnum_current + 1
        print("self.quiz_questions= " + str(len(self.quiz_questions)))
        if self.qnum_current < len(self.quiz_questions):
            print("self.qnum_current = " + str(self.qnum_current))
            current = self.quiz_questions[self.qnum_current]
            # Show question
            row_content = current.split(",")
            question_type = row_content[0].strip()
            question_imgfile = row_content[1].strip()
            question_equation = row_content[2].strip()
            question_statement = row_content[4].strip()
            self.q.configure(
                text=f"Q{self.qnum_current + 1}: {question_equation}")
            self.q_statement.configure(text=f"{question_statement}")
            if question_type == 'i':
                # Show image
                try:
                    # self.img_lod = ctk.CTkImage(Image.open(question_imgfile),size=(125,200,Image.LANCZOS))
                    self.img_init = Image.open(question_imgfile)
                    og_width, og_height = self.img_init.size
                    new_width = int(og_width * 0.25)
                    new_height = int(og_height*0.25)
                    # Use a high-quality filter for downsampling
                    resized_img = self.img_init.resize(
                        (new_width, new_height), Image.LANCZOS)
                    self.resized_img = ctk.CTkImage(resized_img)
                    self.img_label.configure(image=self.resized_img)
                except FileNotFoundError:
                    self.img_label.configure(text="Image not found", image='')
                    print(os.path.dirname(__file__) + f" {question_imgfile} ")
            else:
                self.img_label.configure(image='', text='')
        else:
            self.stop_timer()
            messagebox.showinfo(
                "Quiz Finished", f"Congratualtions {self.homepage.stored_username}!, you scored {self.score.get()} correct answers."
                f"\nYou got {self.score.get()}/{len(self.quiz_questions)}correct."
                f"\nTime taken was {self.timer.get()}")
            self.end_quiz()
        self.actual_score = f"{self.score.get()}/{len(self.quiz_questions)}"
    def end_quiz(self): #This function is used for ending the quiz
        self.store_leaderboard_data()
        self.quiz.withdraw() #This throws the quiz window in memory without actually destroying it.
        self.homepage.deiconify() #Here I bring the home window back from memory, deiconfiy() retrieves the home window from memory. 
        self.leaderboard.create_leaderboard_window() #This is where the creation of the leaderboard window is done. 
        print("Creating leaderboard window")
        print("Leaderboard widgets loaded")
    def return_home_quiz(self):
            exit_home = messagebox.askyesno("Return to home","Would you like to exit the quiz")
            if exit_home == 1:
                global timer_state
                timer_state = 0
                self.quiz_questions = []
                self.qnum_current = -1
                self.difficulty.difficulty_chosen = False
                self.quiz.destroy()
                self.homepage.deiconify()
                self.homepage.reset_game_state_quiz()

    # This function is used to check if the students input matches the correct or wrong answer to the question.
    def check_answer(self): #This function is used to check if the students input matches the correct or wrong answer to the question. 
        student_input = self.q_response.get().strip()
        print("Program collecting user input")
        self.correct_ans = self.quiz_questions[self.qnum_current].split(",")[3]
        if student_input == self.correct_ans: #Answer validation
            self.score_increment()
            print("Score increased,correct answer")
            self.q_response.delete(0,END)
            self.show_next_question()
        elif len(student_input) ==0:
            self.stop_timer()
            print("Answer contains blanks")
            messagebox.showwarning("Warning","Answer field cannot be left blank")
            self.start_time()
            return
        elif len(student_input) > 30:
            self.stop_timer()
            messagebox.showwarning("Warning","Answer cannot be above 30 characters")
            self.start_time()
            print("Character limit exceeded")
            return
        elif " " in student_input:
            print("Whitespaces")
            messagebox.showwarning("Warning","No spaces between your answer")
            self.start_time()
            return
        else:
            print("Score did not increase,incorrect answer")
            self.q_response.delete(0, tk.END)
            self.show_next_question()

    def store_leaderboard_data(self):
        # Store the filename of the users details to a variable.
        f_path = "leaderboard_details.json"
        # Create a blank list for the users details, certain criteria is appended later.
        lb_details = [] #lb - short for leaderboard, here we initialise a blank list which is updated later onwards.
        print("init list for storing details needed for the leaderboard")
        lb_details.append([self.homepage.stored_username,self.homepage.stored_qamount, #Appending username, question amount the user selected.
                           #These details are later on used for the leaderboard
                           self.difficulty.difficulty_level,self.actual_score,self.timer.get()]) #Appending the difficulty level, the score and time taken to this list specifically used to display certain criteria on the leaderboard.
        try:
            with open(f_path, 'r') as file:
                lb_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            lb_data = []

        lb_data.append(lb_details)

        with open(f_path, 'w') as file:
            json.dump(lb_data, file, indent=4)


class Leaderboard():
    def __init__(self, difficulty_inst, quiz_inst, home_inst):
        self.difficulty = difficulty_inst
        # We are accessing the Quiz class by creating this instance variable.
        self.quiz_page = quiz_inst
        self.homepage = home_inst
    def create_leaderboard_window(self):
        # Global Variables for the class
        self.leaderboard = Toplevel(self.homepage)
        self.leaderboard.title("Leaderboard")  # Set the window title
        self.leaderboard.config(bg="#b4cbed")
        self.leaderboard.geometry("680x520")  # Set the window size
        self.leaderboard.resizable(False,False)
        self.leaderboard.protocol("WM_DELETE_WINDOW",self.close_leaderboard)
        #Row and column configuration
        self.leaderboard.grid_rowconfigure(0,weight=1)
        self.leaderboard.grid_columnconfigure(0,weight=1)
        self.create_leaderboard()
        self.display_lb_data()
    def create_leaderboard(self): #Function which sets up the leaderboard (treeview)
        self.tree = ttk.Treeview(self.leaderboard, columns=("rank", "player", "score","time","difficulty"), show="headings") #Assign the column ids for each field in the leaderboard and show the headings.
        style = ttk.Style() #Initialise style object for leaderboard
        style.theme_use('default')
        style.configure('Treeview', background='#9dbbe7',fieldbackground="#d3ddec", foreground='black', rowheight=25,) #Configure the leaderboard sty
        style.configure('Treeview.Heading',background='#7ba3d1', font=('Lexend',12,'bold')) 
        self.tree.heading("rank", text="Rank")
        self.tree.heading("player", text="Player Name")
        self.tree.heading("score", text="Score")
        self.tree.heading("time", text="Time")
        self.tree.heading("difficulty", text="Difficulty Played")
          # Configure column properties
        self.tree.column("rank", width=40,anchor=tk.CENTER)
        self.tree.column("player", width=80, anchor=tk.CENTER)
        self.tree.column("score", width=50, anchor=tk.CENTER)
        self.tree.column("time",width=120,anchor=tk.CENTER )
        self.tree.column("difficulty",width=80,anchor=tk.CENTER)
        self.tree.grid(row=0,column=0,sticky='nsew')
        print("")
    def close_leaderboard(self):
        self.leaderboard.destroy()
        if self.quiz_page.end_quiz == True:
            self.homepage.reset_game_state_quiz()
    def display_lb_data(self):
        try:
            print("reading in the leaderboard_details json now...")
            with open("leaderboard_details.json", "r", encoding='utf-8') as file:
                    self.leaderboard_data = json.load(file)
                    print(f"loaded {len(self.leaderboard_data)} entries.")
                    print("appended content from json file")
        except (FileNotFoundError, json.JSONDecodeError):
            self.leaderboard_data = []
        for item in self.tree.get_children():
            self.tree.delete(item)
        for rank, entry in enumerate(self.leaderboard_data,1):
            inner_array = entry[0]
            player_name = inner_array[0]
            question_amount = inner_array[1]
            difficulty_mode = inner_array[2]
            actual_score = inner_array[3]
            time_taken = inner_array[4]
            self.tree.insert('','end',values=(rank,player_name,actual_score,time_taken,difficulty_mode))

def main():
    # Setting up class instances
    # An instance variable for the 'Difficulty' class has been created, "None" is passed in the arguments as the other classes do not exist currently
    difficulty_window = Difficulty(None, None, None)
    quiz_window = Quiz(difficulty_window, None, None)
    leaderboard_window = Leaderboard(difficulty_window, quiz_window, None)
    home_window = Home(difficulty_window, quiz_window, leaderboard_window)

    # Linking the remaining classes - use the correct attribute names
    # Store a reference of the Quiz class to the Difficulty class. The Difficulty class can access attributes such as methods,variables, functions from the Quiz class.
    difficulty_window.quiz = quiz_window
    # Store a reference of the leaderboard class to the Difficulty class. The Difficulty class can access attributes such as methods,variables, functions from the Leaderboard class.
    difficulty_window.leaderboard = leaderboard_window
    # Store a reference of the Home class to the Difficulty class. The Difficulty class can access attributes such as methods,variables, functions from the Home class.
    difficulty_window.homepage = home_window
    # Store a reference of the leaderboard class to the Quiz class. The Quiz class can access attributes such as methods,variables, functions from the Leaderboard class.
    quiz_window.leaderboard = leaderboard_window
    # Store a reference of the Home class to the Quiz class. The Quiz class can access attributes such as methods,variables, functions from the Home class.
    quiz_window.homepage = home_window
    leaderboard_window.homepage = home_window  # Use 'homepage' not 'home'
    leaderboard_window.quiz_page = quiz_window  # Use 'quiz_page' not 'quiz'

    print("Opening Homepage...")
    home_window.create_home()
    home_window.bind("<Alt-q>", home_window.kill_event)
    # When the keybind Alt Q is detected, program will terminate, it refers to function kill_event()
    home_window.bind("<Alt-d>", home_window.create_difficulty_window)
    home_window.home_button_setup()
    warnings.filterwarnings("ignore", message=".*Given image is not CTkImage.*", category=UserWarning)
    home_window.mainloop()
main()
