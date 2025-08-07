import customtkinter as ctk
import tkinter as tk
import random,sys,csv,time,os,warnings,json,webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageDraw , ImageTk
global timer_state, qnum
timer_state = 1  # The timer has 2 states , if timer_state is set to 1 the timer is active, if it is 0 the timer is stopped.
ctk.set_appearance_mode("light") #Set the appearance mode of the program
ctk.set_default_color_theme('program_theme.json') # Set the color theme of the program
# Home Window
class Home(ctk.CTk):  # Initialise a class for the main window.
    def __init__(self, difficulty_inst, quiz_inst, leaderboard_inst): #This is the main constructor, this is where all the class instance variables are passed in. 
        super().__init__()
        self.difficulty_mode = difficulty_inst # Create instance variable for Difficulty class so functions, variables from that can be accessed.
        self.quiz = quiz_inst # Create instance variable for Quiz class so functions and variables from that can be accessed.
        self.leaderboard = leaderboard_inst # Create instance variable for Leaderboard class so functions and variables from that can be accessed.
        # self.difficulty_mode = Difficulty(self) #Create instance variable for Difficulty class so functions, variables from that can be accessed.
        # self.quiz = Quiz(self) #Create instance variable for Quiz class so functions and variables from that can be accessed.
        self.pdf_path = "user_guide.pdf" # Create a variable for storing the user guide path.

    def create_home(self):  # This function is for setting up the main window.
        self.title("Quavers Teaching Dilemma") # Set the window title.
        self.geometry("680x520") # Set the window size.
        self.config(bg="#b4cbed") # Set the window background.
        self.resizable(False, False) # Disable window resizing.
        self.iconbitmap("qd16x16_log1.ico") # Set the window icon for the root window.
        self.iconphoto(True, PhotoImage(file='qd16x16_logo1.png')) # Set the window icon for all windows.
        # Row and column configurations for the home window 
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0, minsize=300, uniform='a')
        self.my_img = ctk.CTkImage(Image.open(
            "QDLogo3_transp.png"), size=(300, 300, Image.LANCZOS)) # A CTKImage object is created so that the logo file can be loaded in and dimensions can be set, as well as resampling.
        self.img_label = ctk.CTkLabel(
            self, bg_color="#9dbbe7", text='', image=self.my_img) # A CTKLabel object needs to be created in order for the image to actually be displayed, CTKImage objects do not act as labels.
        self.img_label.grid(row=0, column=0, sticky='w') # Display the image on the main window.

    def widget_seperation(self): #Function for creating the divider/ separator on the main window.
        img = Image.new("RGBA", (200, 500), (180, 203, 237, 255))
        draw = ImageDraw.Draw(img)

        top = (100, 0)
        bottom = (100, 500)

        # Draw the 4 sides using lines
        draw.line([top, bottom], fill="black", width=10)        # Draw the line
        self.border = ctk.CTkImage(light_image=img, size=(200, 500))

    # This function is for setting up all the widgets on the home window.
    def home_button_setup(self):
        self.widget_seperation()
        self.border_lbl = ctk.CTkLabel(self,image=self.border, text = "" ) # Create label object for the divider so that it can be displayed.
        self.border_lbl.grid(row=0,column=1,columnspan=1,rowspan=1,padx=(0,200),pady=(10,0),sticky='nsew',) # Position the divider object on the home window.
        self.username_lbl = ctk.CTkLabel(self, width=90,text="Username",font=("Lexend",14,'bold'),bg_color="#9dbbe7") 
        # Create label object for the username label and set configurations(font, background).
        self.username_lbl.grid(row=0,column=(1),rowspan=1,padx=(0,200),pady=(50,0), sticky = "ne") # Display the username entry label on the main window. 
        self.username_entry = ctk.CTkEntry(self,width = 130,bg_color="#b4cbed",font=("Lexend",14,'bold')) 
        # Create an entry object for the username, so the user can actually enter a username.
        self.username_entry.grid(row=0,column=1,columnspan=1,padx=(0,50),pady=(50,0),sticky='ne') # Position the username entry on the home window. 
        self.qamount_lbl = ctk.CTkLabel(self, width=90,text="Question Amount",font=("Lexend",14,'bold'),bg_color="#9dbbe7") 
        # Create a label for the question amount selector and apply configurations.
        self.qamount_lbl.grid(row=0,column=1,rowspan=1,padx=(0,50),pady=(196,0), sticky = 'n') # Display the question amount selector label on the home window. 
        self.qamount_selector = ctk.CTkComboBox(self,values=['3','10','15'],font=("Lexend",14,"bold"),bg_color="#b4cbed",state='readonly')
        # Create a combobox object, this is the object used to create a drop down selection, here the user can select how many questions they want to go through.
        self.qamount_selector.set("") # Set the value of the combobox to an empty string when the program is loaded.
        self.qamount_selector.grid(row=0,column=1,columnspan=1,padx=(0,20),pady=(0,90),sticky='e') # Display the question amount selector on the home window. 
        self.leaderboard_button = ctk.CTkButton(self, text="Leaderboard",font=("Lexend",14,'bold'),width=140,bg_color="#b4cbed",command = self.leaderboard.create_leaderboard_window)
        # Create a button for accesing the Leaderboard from the home screen. This button uses a command from the 'Leaderboard' class, which is where the initiation of the leaderboard window is done.
        self.leaderboard_button.grid(row=0, column=1,ipadx=10,ipady=10,padx=(0,75), pady=(0,160),rowspan=1,sticky='se') # Display the Leaderboard button on the home window.
        self.difficulty_button = ctk.CTkButton(self, text="Choose Difficulty",font=("Lexend",14,'bold'),width=140,bg_color="#b4cbed", command=self.create_difficulty_window) 
        # Similar to the leaderboard button, a button for accesing the difficulty selection screen has been made. 
        self.difficulty_button.grid(row=0, column=1,ipadx=10,ipady=10,padx=(0,75), pady=(0,80),rowspan=1,sticky='se') # Display the "Choose Difficulty" button on the home window. 
        self.quiz_button = ctk.CTkButton(self, text="Start the Quiz!",font=("Lexend",14,'bold'),bg_color="#b4cbed", command=self.create_quiz_window) #
        self.quiz_button.grid(row=0, column=1,ipadx=10,ipady=10,rowspan=3,sticky='se',padx=(0,75)) # Display the "Start Quiz" button on the home window.
        self.help = ctk.CTkButton(self, text="Help",font=("Lexend",14,'bold'),bg_color="#b4cbed",command=self.access_user_guide) 
        # This button has been made so that the end user can access the user guide
        self.help.grid(row=0,column=0,sticky='sw',ipady=10,ipadx=10,padx=(70,0)) # Display the "Help" button on the home window

    # This function is for opening the user guide
    def access_user_guide(self,event=None): # Like any other function in this code we pass 'self' into the parantheses
                                            # What event=None means - The event function is set as none unless an event is executed, in this case if Ctrl + h is pressed, then the event becomes active.
            if os.path.exists(self.pdf_path): # This line of code is for checking if the pdf exists.
                webbrowser.open(self.pdf_path) # Using the webbrowser module, if the pdf exists, then webbrowser will open the pdf in a PDF reader.
            else:
                messagebox.showinfo("Error",f"Could not locate {self.pdf_path}.") # This statement is executed if the pdf is not found. 
    def kill_event(self, event): # This function is specifc to the keybind set (Ctrl + q) for terminating the home window, this is later on referenced at the end of this code file. 
        sys.exit(0) # Terminate the program entirely from the main window. 
    def clear_widgets(self): # This function is used for clearing all input inside of the Combobox and Entry widgets on the home window. 
        for widget in self.winfo_children(): 
            if isinstance(widget,ctk.CTkEntry): # Program checks if the Entry widget is found on the home window.
                widget.delete(0,END) # If the above statement is true, the program then clears the Entry widget. 
            if isinstance(widget,ctk.CTkComboBox): # Program checks if the combobox widget is found on the home window.
                widget.set("") # If the above statement is true, the program then sets the Comboboxes value to an empty string. 
    def reset_game_state_quiz(self): # This function resets the game state to its initial state when a quiz is exited. 
        self.quiz.timer_state = 0 # Timer is stopped when this variable is set to 0.
        self.difficulty_mode.difficulty_chosen = False # Difficulty is set to false, the chosen difficulty is clearerd.
        self.difficulty_mode.quiz_questions = [] # The list of questions inside the difficulty class is cleared
        self.quiz.quiz_questions = [] # The list of questions inside the quiz class is cleared.
        self.quiz.qnum_current = -1 # The current question number is set to -1
        self.clear_widgets() # All input on the quiz window is cleared. 

    def reset_game_state_home(self): # This function resets the game state to its initial state when the home screen is accessed.
        self.quiz.timer_state = 0 # Timer is stopped when this variable is set to 0
        self.difficulty_mode.difficulty_chosen = False # Difficulty mode is set to unchosen
        self.difficulty_mode.quiz_questions = [] # The list of questions inside the difficulty class is cleared
        self.quiz.quiz_questions = [] # The list of questions inside the quiz class is cleared
        self.quiz.qnum_current = -1  # The current question number is set to -1.

    # Function made so that difficulty window can be accessed when the 'Difficulty' button is clicked.
    def create_difficulty_window(self,event=None): # This function is called when the 'Difficulty' button is clicked, it calls the create_difficulty function from the difficulty class.
        # The event=None parameter is so that the function can be called when a certain keyboard shortcut is pressed. 
        self.difficulty_mode.create_difficulty() # Calls the create_difficulty function from the difficulty class.

    def create_quiz_window(self,event=None): # This function, create_quiz_window, checks if a username is valid, a question amount is selected, and a difficulty level is chosen before proceeding to create a quiz window.
        if self.username_validator() == True: # The program calls the username_validator function to check if the username is valid.
            if len(self.qamount_selector.get()) != 0: # The program checks if a question amount has been selected.
                if self.difficulty_mode.difficulty_chosen == True: # The program checks if a difficulty level has been chosen.
                    self.store_user_details() # The program calls the store_user_details function to store the username and question amount.
                    self.stored_username = self.username_input # The program sets the stored_username variable to the username input(self.username_entry.get().strip()).
                    self.stored_qamount  = self.qamount_selector.get() # The program sets the stored_qamount variable to the question amount selected(self.qamount_selector.get()).
                    self.quiz.quiz_questions = self.difficulty_mode.quiz_questions # The program sets the quiz_questions variable in the quiz class to the quiz_questions variable in the difficulty class.
                    self.clear_widgets() #Call the clear_widgets() function to clear all input on the home window.
                    self.withdraw() #Call the withdraw() function to withdraw the home window from memory.
                    self.quiz.create_questions_window() #Call the create_questions_window() function from the quiz class to create the quiz window.
                elif self.difficulty_mode.difficulty_chosen == False: # The program checks if a difficulty level has not been chosen.
                    messagebox.showwarning(
                        "Warning", "You cannot start the quiz without selecting a difficulty") # The program displays a warning message to the user.
                    # This tells the user that they cannot start the quiz without selecting a difficulty.
            else:  # The program checks if a question amount has not been selected.
                messagebox.showwarning(
                    "Warning", "You cannot start the quiz without selecting how many questions") # The program displays a warning message to the user.
                # This tells the user that they cannot start the quiz without selecting how many questions.

    # Function used to check for certain cases in the username input.
    def username_validator(self): # This function checks for certain cases in the username input.
        self.username_input = str(self.username_entry.get().strip()) # The program sets the username_input variable to the username input(self.username_entry.get().strip()).
        if len(self.username_input) == 0: # The program checks if the username input is empty.
            messagebox.showwarning("Warning", "Name must not be left blank") # Display an error message if username is empty.
            return False 
        # Iterate through each character in the username input and check if there are characters which are not alphabetical.
        elif not any(char.isalpha() for char in self.username_input): # The program checks if there are characters which are not alphabetical.
            messagebox.showwarning("Warning", "Username must contain at least one letter.\nProgram will not accept inputs that contain only numbers and symbols.")
            # Display an error message if username does not contain at least one letter.
            return False # The program returns False if the username input is invalid.
        elif " " in self.username_input: # The program checks if there are whitespaces in the username input.
            messagebox.showwarning("Warning", "There should be no whitespaces in the username..\nProgram will remove the whitespaces found.") 
            # Display an error message if username contains whitespaces.
            self.username_entry.delete(0, END) # The program deletes the whitespaces from the username input.
            self.username_entry.insert(0, self.username_input.replace(" ", "")) # The program replaces the whitespaces with an empty string.
            return False # The program returns False if the username input is invalid.
        elif len(self.username_input) > 12: # The program checks if the username input is greater than 12 characters.
            messagebox.showwarning("Warning", "Username cannot be above 12 characters.\nIt has been shortened to 12 characters now.")
            # Display an error message if username is greater than 12 characters.
            self.username_entry.delete(0, END) # The program deletes the username input.
            self.username_entry.insert(0, self.username_input[:12]) # Truncate the username input to 12 characters.
            return False # The program returns False if the username input is invalid.
        elif len(self.username_input) < 4: # The program checks if the username input is less than 4 characters.
            messagebox.showwarning("Warning", "Username cannot be less than 4 characters ")
            # Display an error message if username is less than 4 characters.
            return False # The program returns False if the username input is invalid.
        else:
            return True # The program returns True if the username input is valid.

    def store_user_details(self): # This function is for storing the user details.
        f_path = "user_details.json" # Store the filepath of where the user details will be stored, to a variable.
        user_details = [] # Initialise an empty list for the users details.
        # Append user details (username, question amount, and difficulty level) to the list
        user_details.append([self.username_input, self.qamount_selector.get(
        ), self.difficulty_mode.difficulty_level]) 
        try: 
            # Attempt open the user details file in read mode.
            with open(f_path, 'r') as file: 
                user_data = json.load(file) # Load the data from the user_details.json file.
        except (FileNotFoundError, json.JSONDecodeError):  
            # If the file does not exist or data is corrupted, initialize an empty list
            user_data = [] 

        user_data.append(user_details)  # Append the user_details list to the existing data.

        with open(f_path, 'w') as file: # Open the user_details.json file again, but this time for writing. JSON handles appending differently compared to regular text files.
            json.dump(user_data, file, indent=4) # Write the updated data to the file with indentation

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
        self.difficulty.config(background="#d9e4f4")
        self.difficulty.title("Select Difficulty")
        self.difficulty.geometry("400x250")
        self.difficulty.resizable(False,False) #Prevent the user from being able to resize the window
        # Configure the grid for the difficulty window
        self.difficulty.columnconfigure(0,weight=1)
        self.difficulty.columnconfigure(1,weight=0)
        self.difficulty.rowconfigure(0,weight=0)
        self.difficulty.rowconfigure(1,weight=0)
     # Button Setup for difficulty window
        self.diff_button_setup()
    def diff_button_setup(self): # Function for setting up all widgets on the difficulty window.
        self.button_frame = ctk.CTkFrame(self.difficulty,fg_color="#9dbbe7") 
        # Create a frame to hold the buttons, and set its foreground color to a light blue. 
        self.button_frame.grid(row=1,column=0,sticky='ew',padx=20,pady=5) # Add the frame to the grid layout.
        # Set the frame's position in the grid, spanning the entire width and with padding.
        self.difficulty_mode_colors = [  # Define a list of colors for the difficulty mode buttons.
            '#11A800', '#DDFF00', '#820000', "#A161AF"] # These colors will be used for the buttons' background colors.
        for entry in range(len(self.difficulty_modes)): # Iterate over the range of difficulty modes.
            buttons = ctk.CTkButton(self.button_frame, # Create a new button for each difficulty mode.
                                         text=self.difficulty_modes[entry],
                                         font=("Lexend", 16),
                                         border_width=2,
                                         fg_color=self.difficulty_mode_colors[entry],
                                         text_color="#000000",
                                         command=lambda i=entry: self.read_difficulty_file(i))
            # Set the button's text, font, border width, background color, text color, and command.
            buttons.grid(row=entry,column = 0,pady=7,padx=66) # Set the button's position in the grid, with padding and spacing.

    def read_difficulty_file(self, listIndex):
        # Here the program is storing the condition that the user has chosen a difficulty and is true.
        self.difficulty_chosen = True
        self.difficulty_level = self.difficulty_modes[listIndex]
        myFile = self.myquiz_filepath + self.csvFiles_Names[listIndex]
        # Program initiates a blank list for all content related to the questions
        self.quiz_questions = []
        with open(myFile, "r", encoding='utf-8') as file:  # Open the CSV file in read mode with UTF-8 encoding.
            for line_number, line_content in enumerate(file, 0): # Iterate over each  line in the file, starting from line 0.
                # Append all content per row inside of the csvfiles to the quiz questions list, converting the content to lowercase.
                self.quiz_questions.append(line_content.lower())
        # Shuffle the questions around to provide more playability.
        random.shuffle(self.quiz_questions)
        selected_amount = int(self.homepage.qamount_selector.get()) # Get the selected question amount from the home windows, question amount selector.
        self.quiz_questions = self.quiz_questions[:selected_amount] # Trim the quiz questions list to the selected amount.
        self.difficulty.destroy() # Destroy the difficulty selection window. 


# Quiz Window
class Quiz():
    def __init__(self, difficulty_inst, leaderboard_inst, home_inst):
        # Class instance variables
        self.difficulty = difficulty_inst # Create a instance variable for the 'Difficulty' class so attributes from that can be accessed here.
        self.leaderboard = leaderboard_inst # Create a instance variable for the 'Leaderboard' class so attributes from that can be accessed here.
        self.homepage = home_inst  # Create a instance variable for the 'Home' class so attributes from that can be accessed here.
        # This variable is also how the program knows where to create the Toplevel window from. 
        # I create a variable for keeping track of question number, this can be accessed anywhere inside of the class (function)
        self.qnum_current = -1 # Set the current question number to - 1, this is not true in the actual quiz window.
        self.quiz_questions = []  # Initialise an empty list for keeping track of the questions
        # This list will be populated with questions later in the program.


    # Function for creating the questions page
    def create_questions_window(self):
        # Create a new Toplevel window for the quiz window. 
        self.quiz = Toplevel(self.homepage) # Set the parent window to the homepage.
        self.quiz.protocol("WM_DELETE_WINDOW", self.return_home_quiz) # Set up the window close protocol to return to the homepage.
        self.quiz.config(bg="#b4cbed") # Set the background color of the window.
        self.quiz.title("Questions")  # Set the window title.
        self.quiz.geometry("680x520")  # Set the window size.
        self.timer_setup() # Initialise the timer setup.
        global timer_state # Set the global timer state to 1.
        timer_state = 1
        self.timer_init() #Initialise the timer.
        self.score_setup() #Set up the score system.
        self.start_ques() # Start the quiz by initializing the first question.
        self.show_next_question() # Function for showing the next question method. 

    def start_ques(self):
        self.q = ctk.CTkLabel( # Create a labe; to display the question.
            self.quiz, text="", text_color="#000000", font=("Lexend", 16, "bold")) # Set labels text color and font. 
        self.q.grid(row=4, column=3) # Apply the positioning of the label.
        self.q_statement = ctk.CTkLabel(  # Create a label to display the question statement.
            self.quiz, text="", text_color="#000000", font=("Lexend", 16, "bold")) # Set labels text color and font.
        self.q_statement.grid(row=5, column=3) # Add the label to the grid layout using row and column.
        self.q_response = ctk.CTkEntry(self.quiz, font=("Lexend", 14, "bold"))  # Create an entry for the user to input their answer.
        self.q_response.grid(row=6, column=3, columnspan=3, padx=20, pady=40) # Add the entry to the grid layout using row and column.
        self.q_submit = ctk.CTkButton(self.quiz, text="Submit", font=( # Create a button submit the user's answer.
            "Lexend", 16, "bold"), command=self.check_answer) # Set the buttons, text, font and command. 
        self.q_submit.grid(row=8, column=3, padx=20) # Add the button to the grid layout using row and column.
        self.quiz.bind("<Return>",lambda event: self.check_answer()) # Bind the enter key to the check_answer function.
        self.img_label = ctk.CTkLabel(self.quiz, text='')  # Create a label to display the image, it is set as an empty string initially but is later on configured in another method. 
        self.img_label.grid(pady=10) # Add the label to the grid layout using row and column.

    def timer_setup(self):  # Function for setting up the timer
        self.timer = StringVar()  # Initialise a string variable
        # Set the string variable to be 00:00:00 , when Start Quiz button is clicked, timer starts counting upwards from 00:00:00
        self.timer.set("00:00:00")
        # Create a label for the timer
        self.tlabel = ctk.CTkLabel(
            self.quiz, textvariable=self.timer, text_color="#006AAC") # Set the timer text color and text variable.
        self.tlabel.configure(font=("Lexend", 18, "bold")
                              )  # Set the timer font
        # Place the timer on the window.
        self.tlabel.grid(row=1, column=3, sticky="ew", padx=60)
    
    def stop_timer(self): # Function for stopping the timer at certain points.
        global timer_state # Set the global timer state to 0.
        timer_state = 0 # Stop the timer.
    def start_time(self): # Function for starting the timer at certain points
        global timer_state # Set the global timer state to 1.
        timer_state = 1 # Start the timer
        self.active_timer() # Call the active_timer method
    def active_timer(self): # Function for activating the timer, this is done by calling the timer_init method.
        global timer_state # Access the global variable tracking the current timer state
        self.timer_init() # Initialise the timer to its starting state. 

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
        self.score = StringVar() # Create a StringVar object to store the current score as a string. 
        self.score.set("0")  # Set the value of this String Variable to 0.
        self.display_score = StringVar() # Create another String Variable for dynamic display and updates. 
        self.display_score.set("Score: " + self.score.get()) # Initialize the displayed score with the initial score (0).
        self.score.trace_add("write", self.update_score) # Add a trace to update the displayed score when the actual score changes.
        self.quiz_scorelab = ctk.CTkLabel( # Create a label to display the score in the quiz window. 
            self.quiz, textvariable=self.display_score, text_color="#006AAC") # Set the text color and text variable for the label.
        self.quiz_scorelab.configure(font=("Lexend", 12, "bold")) # Configure the font of the label.
        self.quiz_scorelab.grid(row=3, column=3) # Add the label to the grid layout using row and column.

    def update_score(self, *args): # Function for updating the score displayed in the GUI.
        self.display_score.set("Score: " + self.score.get()) # Update the displayed score with the current score. 
        #self.score.get() returns the current score as a string.

    def score_increment(self): # Function for incrementing the score.
        current_score = int(self.score.get()) # Get the current score as an integer.
        new_score = str(current_score + 1) # Increment the score by 1 and convert it to a string.
        self.score.set(new_score) # Update the score StringVar with the new score.

    def show_next_question(self): # Function for showing the next question.
        self.qnum_current = self.qnum_current + 1 # Increment the current question number, the program will do this each time a new question is loaded
        if self.qnum_current < len(self.quiz_questions): # Check if the current question number is less than the total number of questions.
            current = self.quiz_questions[self.qnum_current] # Get the current question from the list of questions.
            # Split the current question into its components.
            row_content = current.split(",") #
            question_type = row_content[0].strip() # Get the question type (i for image, e for equation).
            question_imgfile = row_content[1].strip() # Get the image file path.
            question_equation = row_content[2].strip() # Get the question equation.
            question_statement = row_content[4].strip() # Get the question statement.
            self.q.configure( # Configure the question label.
                text=f"Q{self.qnum_current + 1}: {question_equation}") # Set the text of the label to the current question number and equation.
            self.q_statement.configure(text=f"{question_statement}") # Set the text of the question statement label to the question statement.
            if self.qnum_current == len(self.quiz_questions) - 1: # Check if the current question is the last question.
                self.q_submit.configure(text='Finish Quiz') # Change the text of the submit button to "Finish Quiz".
            if question_type == 'i': # Check if the question type is an image.
                # Show the image.
                try: # Try to open the image file.
                    self.img_lod = ctk.CTkImage(Image.open(question_imgfile),size=(125,200,Image.LANCZOS)) # Open the image file.
                    og_width, og_height = self.img_init.size # Get the original width and height of the image.
                    # Use a high-quality filter for downsampling
                    resized_img = self.img_init.resize( # Resize the image.
                        (125,200), Image.LANCZOS)
                    self.resized_img = ctk.CTkImage(resized_img) # Convert the resized image to a CTKImage object.
                    self.img_label.configure(image=self.resized_img) # Configure the image label to display the resized image.
                except FileNotFoundError: # If the image file is not found.
                    self.img_label.configure(text="Image not found", image='') # Configure the image label to display an error message.
            else:
                self.img_label.configure(image='', text='')  # If the question type is not an image, clear the image label.
        else: # When all questions have been shown, the program will follow this set of instructions.
            self.stop_timer() # Stop the timer.
            messagebox.showinfo( # Show an information message box.
            # Display a message indicating the quiz is finished and the score.
                "Quiz Finished", f"Congratualtions {self.homepage.stored_username}!, you scored {self.score.get()} correct answers." 
                f"\nYou got {self.score.get()}/{len(self.quiz_questions)}correct." 
                f"\nTime taken was {self.timer.get()}")
            self.end_quiz() # Call the end_quiz function to end the quiz.
    def end_quiz(self): #This function is used for ending the quiz
        self.actual_score = f"{self.score.get()}/{len(self.quiz_questions)}" # Get the actual score as a string, e.g. (4/5).
        self.store_leaderboard_data() # Call the store_leaderboard_data function to store data which is later used for the leaderboard.
        self.quiz.destroy() # Destroy the quiz window, to prevent further issues from occuring.
        self.homepage.deiconify() # Here I bring the home window back from memory, deiconfiy() retrieves the home window from memory. 
        self.leaderboard.create_leaderboard_window() # This is where the creation of the leaderboard window is done. 
    def return_home_quiz(self): # This function is used to return to the home window from the quiz window.
            exit_home = messagebox.askyesno("Return to home","Would you like to exit the quiz") # Ask the user if they would like to exit the quiz.
            if exit_home == 1: # If the user chooses to exit the quiz.
                global timer_state # Set the global timer state to 0.
                timer_state = 0 # Stop the timer.
                self.quiz_questions = [] # Clear the quiz questions list.
                self.qnum_current = -1 # Set the current question number to -1.
                self.difficulty.difficulty_chosen = False # Set the difficulty mode to unchosen.
                self.quiz.destroy() # Destroy the quiz window.
                self.homepage.deiconify() # Bring the home window back from memory.
                self.homepage.reset_game_state_quiz() # Reset the game state to its initial state.

    # This function is used to check if the students input matches the correct or wrong answer to the question.
    def check_answer(self): #This function is used to check if the students input matches the correct or wrong answer to the question. 
        student_input = self.q_response.get().lower().strip() # Get the students input and convert it to lowercase.
        self.correct_ans = self.quiz_questions[self.qnum_current].split(",")[3] # Get the correct answer from the csvf ile, for the current question.
        if student_input == self.correct_ans: # If the students input matches the correct answer.
            self.score_increment() # Increment the score.
            self.q_response.delete(0,END) # Delete the students input.
            self.show_next_question() # Show the next question.
        elif len(student_input) ==0: # If the students input is empty.
            self.stop_timer() # Stop the timer.
            messagebox.showwarning("Warning","Answer field cannot be left blank") # Show a warning message.
            self.start_time() # Resume the timer, once the messagebox has been dismissed
            return # Return from the function.
        elif len(student_input) > 30: # If the students input is longer than 30 characters.
            self.stop_timer() # Stop the timer.
            messagebox.showwarning("Warning","Answer cannot be above 30 characters") # Show a warning message.
            self.start_time() # Resume the timer, once the messagebox has been dismissed
            return
        elif " " in student_input: # If the students input contains a space.
            messagebox.showwarning("Warning","No spaces between your answer") # Show a warning message.
            self.start_time() # Resume the timer, once the messagebox has been dismissed
            return
        else: # If the students input does match the correct answer.
            self.q_response.delete(0, tk.END) # Delete the students input.
            self.show_next_question() # Call the show_next_question function, so the next question can be displayed.

    def store_leaderboard_data(self): #This function is used to store the leaderboard data
        # Store the filename of the users details to a variable.
        f_path = "leaderboard_details.json" # Store the filepath of where the leaderboard details will be stored, to a variable.
        # Create a blank list for the users details, certain criteria is appended later.
        lb_details = [] # lb - short for leaderboard, here we initialise a blank list which is updated later onwards.
        lb_details.append([self.homepage.stored_username,self.homepage.stored_qamount, # Appending username, question amount the user selected.
                           #These details are later on used for the leaderboard
                           self.difficulty.difficulty_level,self.actual_score,self.timer.get()]) # Appending the difficulty level, the score and time taken to this list specifically used to display certain criteria on the leaderboard.
        try: # Try to open the leaderboard details file.
            with open(f_path, 'r') as file: # Open the file in read mode.
                lb_data = json.load(file) # Load the data from the leaderboard_details.json file.
        except (FileNotFoundError, json.JSONDecodeError): # If the file does not exist or data is corrupted.
            lb_data = [] # Initialise an empty list if the file does not exist, or data is corrupted.

        lb_data.append(lb_details) # Append the users details to the leaderboard data.

        with open(f_path, 'w') as file: # Open the leaderboard_details.json file again, but this time for writing.
            json.dump(lb_data, file, indent=4) # Write the updated data to the file with indentation.


class Leaderboard(): # This class is used to create the leaderboard window
    def __init__(self, difficulty_inst, quiz_inst, home_inst): # Pass class instance variables into the __init__ constructor.
        self.difficulty = difficulty_inst # We are accessing the Difficulty class by creating this instance variable.
        self.quiz_page = quiz_inst # We are accessing the Quiz class by creating this instance variable.
        self.homepage = home_inst # We are accessing the Home class by creating this instance variable.
    def create_leaderboard_window(self,event=None): # This function is used to create the leaderboard window.
        self.leaderboard = Toplevel(self.homepage) # Create a Toplevel window of the parent window (home window).
        self.leaderboard.title("Leaderboard")  # Set the window title.
        self.leaderboard.config(bg="#b4cbed") # Set the background color.
        self.leaderboard.geometry("680x520")  # Set the window size.
        self.leaderboard.resizable(False,False) # Disable the ability to resize the window.
        self.leaderboard.protocol("WM_DELETE_WINDOW",self.close_leaderboard) # Set the protocol to close the window, when the red x on the program window bar is clicked.
        
        #Row and column configuration
        self.leaderboard.grid_rowconfigure(0,weight=0)
        self.leaderboard.grid_rowconfigure(1,weight=1)
        self.leaderboard.grid_columnconfigure(0,weight=1)
        self.leaderboard.grid_columnconfigure(1,weight=0)
        self.create_leaderboard() # Call the create_leaderboard function.
        self.display_lb_data() # Call the display_lb_data function.
    def create_leaderboard(self): #Function which sets up the leaderboard (treeview)
        self.return_homewin = ctk.CTkButton(self.leaderboard, text="Return Home", font=(
            "Lexend", 14, "bold"), command=self.close_leaderboard) # Create a button to return to the home window.
        self.return_homewin.grid(row=0,column=0,sticky='e',padx=90)
        self.return_homewin = ctk.CTkButton(self.leaderboard, text="Remove Entry", font=( # Create a button to remove an entry from the leaderboard.
            "Lexend", 14, "bold"), command=self.tree_row_deletion) # Set text and font for the button, and set the command to the tree_row_deletion function.
        self.return_homewin.grid(row=0,column=0,sticky='w',padx=90) # Place the button in the window.
        self.tree = ttk.Treeview(self.leaderboard, columns=("rank", "player", "score","time","difficulty"), show="headings") #Assign the column ids for each field in the leaderboard and show the headings.
        self.tree.grid(row=1,column=0,sticky='nsew') # Place the treeview in the window.
        style = ttk.Style() #Initialise style object for leaderboard
        style.theme_use('default') # Use the default theme, for the treeview.
        style.configure('Treeview',background='#9dbbe7',fieldbackground="#d3ddec", foreground='black', rowheight=30,) # Configure the treeview style.
        style.configure('Treeview.Heading',background='#7ba3d1', font=('Lexend',12,'bold')) # Configure the treeview heading style.
        self.tree.heading("rank", text="Rank") # Set the heading text for Rank.
        self.tree.heading("player", text="Player Name") # Set the heading text for Player Name.
        self.tree.heading("score", text="Score") # Set the heading text for Score.
        self.tree.heading("time", text="Time") # Set the heading text for Time.
        self.tree.heading("difficulty", text="Difficulty Played") # Set the heading text for Difficulty Played.
          # Configure column properties in the treeview
        self.tree.column("rank", width=60,anchor=tk.CENTER) # Set the width of the Rank column and center align the text.
        self.tree.column("player", width=80, anchor=tk.CENTER) # Set the width of the Player Name column and center align the text.
        self.tree.column("score", width=50, anchor=tk.CENTER) # Set the width of the Score column and center align the text.
        self.tree.column("time",width=120,anchor=tk.CENTER ) # Set the width of the Time column and center align the text.
        self.tree.column("difficulty",width=80,anchor=tk.CENTER) # Set the width of the Difficulty Played column and center align the text.
        scroll_vert = ttk.Scrollbar(self.leaderboard,orient="vertical",command=self.tree.yview) # Create a vertical scrollbar for the treeview.
        scroll_vert.grid(row=1,column=1,sticky='ns') # Place the scrollbar in the window.
        self.tree.configure(yscrollcommand=scroll_vert.set) # Configure the treeview to use the scrollbar.
        self.lock_column_widths() # Call the lock_column_widths function.
    def close_leaderboard(self): # Function used to close the leaderboard window.
        self.leaderboard.destroy() # Destroy the leaderboard window.
        self.homepage.reset_game_state_quiz() # Reset the game state to its initial state.
    def display_lb_data(self): # Display the leaderboard data. 
        try: # Try to load the leaderboard data from a file.
            with open("leaderboard_details.json", "r", encoding='utf-8') as file: # Open the file in read mode.
                    self.leaderboard_data = json.load(file) # Load the data from the file.
        except (FileNotFoundError, json.JSONDecodeError): # If the file does not exist or data is corrupted.
            self.leaderboard_data = [] # Set the leaderboard data to an empty list.
        for item in self.tree.get_children(): # Loop through each item in the treeview.
            self.tree.delete(item) # Delete the item from the treeview.
        for rank, entry in enumerate(self.leaderboard_data,1): # Loop through each entry in the leaderboard data.
            self.inner_array = entry[0] # Get the inner element from the nested list within the leaderboard details file.
            player_name = self.inner_array[0] # Get the player name from the nested list within the leaderboard details file.
            question_amount = self.inner_array[1] # Get the question amount from the nested list within the leaderboard details file.
            difficulty_mode = self.inner_array[2] # Get the difficulty mode from the nested list within the leaderboard details file.
            actual_score = self.inner_array[3] # Get the actual score from the nested list within the leaderboard details file.
            time_taken = self.inner_array[4] # Get the time taken from the nested list within the leaderboard details file.
            self.tree.insert('','end',values=(rank,player_name,actual_score,time_taken,difficulty_mode))
            # Insert the entry into the treeview. 
    def tree_row_deletion(self): #Function used for deleting an entry off the tree
        selected_items = self.tree.selection() # Get the selected row from the treeview, self.tree.selection() is responsible for getting the selected row from the treeview.
        try: # Try to delete an entry from the treeview.
            if not selected_items: # If a row in the treeview is not selected. 
                messagebox.showwarning("Warning","You need to select a row before you can delete it.") # Show a warning message.
            else: # If a row in the treeview is selected.
                entry = selected_items[0] # Get the selected row from the treeview.
                entry_value = self.tree.item(entry,'values') # Get the values of the selected row from the treeview.
                confirm_deletion = messagebox.askyesno("Confirm Action",f"Do you want to proceed with deleting {entry_value[1]}? ") # Ask the user if they want to delete the selected row. For indication, the name contained within the entry has been added to the messagebox.
                if confirm_deletion: # If the user confirms the deletion.
                    selected_entry = int(entry_value[0]) - 1 # Get the index of the selected row from the treeview..
                    self.remove_entry_from_json(selected_entry) # Call the remove_entry_from_json function.
                self.display_lb_data() # Refresh the treeview after the deletion of the entry from the treeview. 
        except Exception:
                messagebox.showwarning("Warning","Please select a row to delete.") # Show a warning message if the row has not been selected.
    def remove_entry_from_json(self,entry_to_remove): # Function used for removing an entry from the json file.
        f_path = "leaderboard_details.json" # Store the filepath of where the leaderboard details will be stored, to a variable.
        try: # Try to open the leaderboard details file in read mode.
         with open(f_path, 'r') as file: # Open the file in read mode.
            removal_lb_data = json.load(file) # Load the data from the file.
         if 0 <= entry_to_remove < len(removal_lb_data): # Program will check if the entry to remove is valid or not. 
            del removal_lb_data[entry_to_remove] # If the entry is valid, remove the entry from the leaderboard details file.
            with open(f_path,'w') as file: # Write the updated data back into the json file with indentation.
                json.dump(removal_lb_data,file,indent=4) # Write the updated data back into the json file.
         else:
            messagebox.showerror("Eror","Entry selection is invalid") # Show an error message if the entry to remove is invalid.

        except(FileNotFoundError, json.JSONDecodeError) as e: 
            messagebox.showerror("Error","The entry was not able to be removed.")

    def lock_column_widths(self): # This function is used to lock the column widths of the treeview.
        fixed_column_widths = { # Define the fixed column widths.
            "rank": 60, # Store the column width of the rank column into this dictionary.
            "player": 80, # Store the column width of the player name column into this dictionary.
            "score": 50, #  Store the column width of the score column into this dictionary.
            "time": 120, # Store the column width of the time column into this dictionary.
            "difficulty": 80 # Store the column width of the difficulty column into this dictionary.
        }
        for col, width in fixed_column_widths.items(): # Loop through each column and width in the fixed column widths dictionary.
            self.tree.column(col,width=width) # The program sets the width of the column to the value of the width variable, col is the name of the column.
        def prevent_resize_columns(event): # This function is used for preventing the user from resizing the columns of the treeview, this stops the window from being dynamically resized.
            cursor_region = self.tree.identify_region(event.x,event.y) # Get the position of the cursor relative to the treeview. 
            if cursor_region == "separator": # The program checks if the position of the co-ordinates is located on the column separators.
                return "break" # returning 'break' means that default keybinds are interrupted.
        self.tree.bind("<Button-1>",prevent_resize_columns) # The prevent_resize_columns is binded to the left mouse button.
        # This is what stops the user from resizing the columns of the treeview.
        self.tree.bind("<B1-Motion>",prevent_resize_columns)  
def main(): # This is the main function, this is where class instance variables are initialised, and the creation of the home window is done. 
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
    leaderboard_window.homepage = home_window  # Store a reference of the 'Home' class to the 'Leaderboard' class. The 'Leaderboard' class can access attributes such as methods,variables, functions from the Home class.
    leaderboard_window.quiz_page = quiz_window # Store a reference of the 'Quiz' class to the 'Leaderboard' class. The 'Leaderboard' class can access attributes such as methods,variables, functions from the Quiz class.
    home_window.create_home() # The program calls the create_home function from the home class. 
    home_window.home_button_setup() # The program calls the home_button_setup function from the home class.c
    # Bind certain functions from the home window to a set of keybinds (Ctrl + d - accesses the difficulty window)
    home_window.bind("<Control-q>", home_window.kill_event) # The program binds the kill_event function from the Home class to the keybind Ctrl + q.
    home_window.bind("<Control-d>", home_window.create_difficulty_window) #The program binds the create_difficulty_window function from the Home class to the keybind Ctrl + d.
    home_window.bind("<Control-h>",home_window.access_user_guide) # The program binds the access_user_guide function from the Home class to the keybind Ctrl + h.
    home_window.bind("<Control-l>",home_window.leaderboard.create_leaderboard_window) # The program binds the create_leaderboard_window function from the Home class to the keybind Ctrl + l
    warnings.filterwarnings("ignore", message=".*Given image is not CTkImage.*", category=UserWarning)
    home_window.mainloop() # It allows the program to loop again.
main() # Call the main function. 
