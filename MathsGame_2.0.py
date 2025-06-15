import customtkinter
from tkinter import *




#Home Window
class Quiz(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Quavers Teaching Dillema")
        self.geometry("450x250")
        self.iconbitmap("")
        self.grid_columnconfigure((0,7),weight=7)
        self.button = customtkinter.CTkButton(self, text="Start",fg_color="#000000",font=customtkinter.CTkFont(family="Quicksand",weight="bold"),command=self.start_click)
        self.button.grid(row=7,column=7,padx=10,pady=10)

        self.combobox = customtkinter.CTkComboBox(self, values=["Easy","Hard"])
        self.combobox.grid(row=2,column=2,padx=20)
    def start_click(self):
        selected_difficulty = self.combobox.get()
        print("debug")  
        print("Selected Difficulty:",selected_difficulty)



mathsquiz = Quiz()
mathsquiz.mainloop()
