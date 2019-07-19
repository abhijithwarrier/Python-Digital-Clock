# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI FOR DIGITAL CLOCK AND DATE USING TKINTER MODULE

# Importing necessary packages
import tkinter as tk
from tkinter import *
from time import strftime

# Defining CreateWidgets() to create widgets for displaying time and date
def Createwidgets():

    # Creating a label for displaying today' date
    root.dateLabel = Label(root, text="DATE : "+strftime("%d/%m/%Y"),
                           font=("Helvetica", 50), bg="skyblue", fg="white")
    # Positioning the date label
    root.dateLabel.grid(sticky="nw")

    # Creating a label for displaying current time
    root.timeLabel = Label(root, font=("Helvetica", 100), bg="skyblue", fg="white")
    root.timeLabel.grid(sticky="news")

    # Calling the updateTime()
    updateTime()

#---

# Defining updateTime() for displaying the time
def updateTime():
    # Configuring the time label to display the current time
    root.timeLabel.config(text=strftime("%H:%M:%S"))

    # CallingupdateTime() after 1 second to display the current time on label
    root.timeLabel.after(1000, updateTime)

# Creating object root of tk
root = tk.Tk()

# Setting the title and background color disabling the resizing property
root.title("DIGITAL CLOCK")
root.config(bg="skyblue")
root.resizable(False, False)

# Calling the CreateWidgets() function
Createwidgets()

# Defining infinite loop to run application
root.mainloop()
