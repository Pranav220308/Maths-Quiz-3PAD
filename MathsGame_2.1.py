import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import Image
import pygame
#Set the theme
ctk.set_appearance_mode("light")
pygame.mixer.init()

#Difficulty Selection
class Difficulty():
    def __init__(self,home):
        self.home = home #Store the parent window to a variable
    def create_d(self):
        self.difficulty = Toplevel(self.home)
        self.difficulty.config(background="#000000")
        self.difficulty.title("Difficulty")
        self.difficulty.geometry("400x250")
        self.difficulty.grid_columnconfigure(0, weight=1)
        self.difficulty.grid_rowconfigure((0, 1), weight=1)
    # Temporary Button Setup for difficulty window
    def button_setup(self):
        
        self.difficulty_Easy = ctk.CTkButton(self.difficulty,fg_color="#11A800",  text="😄 Easy", font=("Segoe UI",16),text_color="#FFFFFF",command=self.close_difficulty_window)
        self.difficulty_Easy.grid(row=0,column=0,padx=10,pady=10)
        self.difficulty_Normal = ctk.CTkButton(self.difficulty,fg_color="#DDFF00", text="😐 Normal",font=("Segoe UI",16),text_color="#000000",)
        self.difficulty_Normal.grid(row=1,column=0,padx=10,pady=10)
        self.difficulty_Hard = ctk.CTkButton(self.difficulty,fg_color="#820000" ,text="😠 Hard",font=("Segoe UI",16),text_color="#FFFFFF")
        self.difficulty_Hard.grid(row=2,column=0,padx=10,pady=10)
        self.difficulty_Extreme = ctk.CTkButton(self.difficulty,fg_color="#470057" ,text="😈 Extreme",font=("Segoe UI",16),text_color="#FFFFFF")
        self.difficulty_Extreme.grid(row=3,column=0,padx=10,pady=10)
    
    def close_difficulty_window(self):
         terminate = self.difficulty.destroy()
         print("Selected Difficulty:",self.difficulty_Easy._text)
         terminate
        
#Home Window
class Home(ctk.CTk):
    def __init__(self):
        super().__init__() 
        self.title("Quavers Teaching Dillema")
        self.geometry("400x250")
        self.config(bg="#f7f4e4")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=1,column=0,padx=20,pady=20)
        self.username_entry = ctk.CTkLabel(self, text="Username")
        self.username_entry.grid(row=0,column=0)
        self.button = ctk.CTkButton(self, text="my button", command=self.create_difficulty_window)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.button1 = ctk.CTkButton(self, text="PLAY", command=self.play_music_player)
        self.button1.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.button2 = ctk.CTkButton(self, text="STOP", command=self.paused_music_player)
        self.button2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    

    def create_difficulty_window(self):
        print("Window Creating...")
        difficulty_window = Difficulty(self)
        difficulty_window.create_d()
        print("Window Created")
        difficulty_window.button_setup()

    #Music Player
    def play_music_player(self):
                pygame.mixer.music.load("My Innermost Apocalypse.mp3")
                pygame.mixer.music.play()

    def paused_music_player(self):
                pygame.mixer.music.pause()       
home_page = Home()
home_page.mainloop()

