    # Importing Required Libraries and modules
from random import sample
from customtkinter import *
from PIL import Image
from time import sleep
from tkinter import messagebox as msg

# Creating object of customtkinter to create window
win = CTk()

# Main Class Generator 
class Generator():
    # Creating Variables
    width = 500
    height = 520
    # Variable for generating random password
    numbers = "01234567890123456789"
    CapsLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTYVWXYZ"
    smallLetters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    speicalLetters = """!@#$%^&*(-=+_""'':;/?.>,<` `~{[}]\\|')"""

    # Constructor
    def __init__(self):
        win.geometry(f"{self.width}x{self.height}")
        win.resizable(0, 0) # Make window non-resizeable

        # Adding Icon 
        win.wm_iconbitmap(r"Bin\\PasswordGeneratorLogo.ico")
        win.eval('tk::PlaceWindow . center') # Make window remain in center
        win.title("Password Generator") # Title 

        # Variables for storing Entry data
        self.strength = StringVar()
        self.length = StringVar()
        self.type = StringVar()

        # Initializing of the elements to be setup
        self.setElement()

    # Method to setup required Elements
    def setElement(self):
        # Adding label for Title in window
        CTkLabel(win, text="", image=CTkImage(Image.open("Bin/PasswordGeneratorText.png"), size=(400, 200))).place(x=50, y=0)
        CTkLabel(win, text="", image=CTkImage(Image.open("Bin/PasswordGeneratorVerificationLogo.png"), size=(50, 50))).place(x=2, y=5)

        # Adding label and dropdown for Strength
        CTkLabel(win, text="Choose Strength:").place(x=15, y=202)
        self.Strength = CTkOptionMenu(win, fg_color="#4CFFC2", text_color='black', variable=self.strength, values=["Simple", "Strong", "Very Strong"], command=self.Check)
        self.Strength.place(x=10, y=240)
        self.strength.set("Simple") # Setting strength to Simple by default

        # Adding label and dropdown for Length
        CTkLabel(win, text="Choose Length:").place(x=200, y=202)
        self.Length = CTkOptionMenu(win, fg_color="#4CFFC2", text_color='black', variable=self.length, values=[str(x) for x in range(8, 21)])
        self.Length.place(x=200, y=240)
        self.Length.set("8") # Setting strength to 8 by default

        # Adding lable and radiobuttons for selection of type:
        self.choice = CTkLabel(win, text="Choose Type:")
        self.r1 = CTkRadioButton(win, fg_color="#4CFFC2", text_color='black', text="Numeric", variable=self.type, value="Numeric")
        self.r2 = CTkRadioButton(win, fg_color="#4CFFC2", text_color='black', text="Alphabetical", variable=self.type, value="Alphabetical")

        # Adding label to display password
        self.Pass = CTkLabel(win, text="", font=("Lucida Handwriting", 20))
        self.Pass.place(x=100, y=420)

        # Creating Submit, Clear and Copy Button
        self.submitbtn =  CTkButton(win, fg_color="#4CFFC2", text_color='black', text="Submit", command=self.setEntry)
        self.submitbtn.place(x=10, y=480)
        CTkButton(win, fg_color="#4CFFC2", text_color='black', text="Clear", command=self.Clear).place(x=180, y=480)
        self.cpybtn = CTkButton(win, fg_color="#4CFFC2", text_color='black', text="Copy", state=DISABLED, command=self.Copy)
        self.cpybtn.place(x=350, y=480)
    
    # Method to show and hide type label and radiobuttons
    def Check(self, event):
        pass
        if self.strength.get() == "Simple":
            self.choice.place(x=350, y=202)
            self.r1.place(x=350, y=232)
            self.r2.place(x=350, y=262)
        if self.strength.get() == "Strong" or self.strength.get() == "Very Strong":
            self.r1.place_forget()
            self.r2.place_forget()
            self.choice.place_forget()

    # Method to Create frame and entries, displaying the password in entries
    def setEntry(self):
        if self.type.get()=="" and self.strength.get()=="Simple":
            # If all details are not filled then a message will pop up to fill them
            msg.showwarning("Missing Details", "Please Fill all the fields")
        else:
            # Creating Frame
            self.frame = CTkFrame(win, fg_color="transparent", width=450, height=100, border_width=None)
            self.frame.place(x=10, y=292)
            # Evaluating the length of password
            self.Len = int(self.length.get())
            # Creating a nested list to store entries
            self.List = [[x, StringVar()] for x in range(self.Len)]
            # Creating Entries
            for i in range(self.Len):
                if i <= 9:
                    CTkEntry(self.frame, width=40, height=50, state=DISABLED, textvariable=self.List[i][1], border_color="black", text_color="white", fg_color="black").grid(row=0, column=i, padx=4)
                else:
                    CTkEntry(self.frame, width=40, height=50, state=DISABLED, textvariable=self.List[i][1], border_color="black", text_color="white", fg_color="black").grid(row=1, column=i-10)
            self.submitbtn.configure(state=DISABLED)
            # Animating the password input in entries
            self.password = self.generatrePass()
            self.cpybtn.configure(state=NORMAL)
            self.k = 0
            self.n = 0
            j = 1000
            while self.n != self.Len:
                win.after(j, self.fun)
                j += 300
                self.n += 1

    # Method to set the password one by one at each entry
    def fun(self):
        self.List[self.k][1].set(self.password[self.k])
        if self.k != self.Len-1:
            self.k +=1
        else:
            self.Pass.configure(text=self.password)

    # Method to clear all the details
    def Clear(self):
        pass
        self.length.set("8")
        self.strength.set("Simple")
        self.type.set("")
        try:
            for widgets in self.frame.winfo_children():
                widgets.destroy()
            self.List.clear()
            self.frame.place_forget()
        except:pass
        self.submitbtn.configure(state=NORMAL)
        self.cpybtn.configure(state=DISABLED)
        self.Pass.configure(text="")

    # Method for generating password
    def generatrePass(self):
        if (self.strength.get() == "Simple"):
            if (self.type.get() == "Numeric"):
                # Generating random password using sample and returning it
                return "".join(sample(self.numbers, self.Len))
            elif (self.type.get() == "Alphabetical"):
                return "".join(sample(self.CapsLetters+self.smallLetters, self.Len))
            else:
                msg.showwarning("Missing Detials", "Please! Select the type")
        elif (self.strength.get() == "Strong"):
            return "".join(sample(self.CapsLetters+self.smallLetters+self.numbers, self.Len))
        elif (self.strength.get() == "Very Strong"):
            return "".join(sample(self.speicalLetters+self.CapsLetters+self.smallLetters+self.numbers, self.Len))
    
    # Method to Copy the password to the clipboard
    def Copy(self):
        win.clipboard_clear()
        win.clipboard_append(self.password)

if __name__ == "__main__":
    gen = Generator()
    win.mainloop()