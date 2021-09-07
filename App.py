
#created using https://www.youtube.com/watch?v=jE-SpRI3K5g

#Imports
import tkinter as tk
from tkinter import filedialog, Text
import os

#Create Window, Disable Window Resizing, Create window title
root = tk.Tk()
root.resizable(False, False) 
root.title("Run Your Apps Quickly!")
#create apps list
apps = []





def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="light blue")
        label.pack()


def runApps():
    for runall in apps:
        os.startfile(runall)


canvas = tk.Canvas(root, height=700, width=700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Open File", padx=25,
                     pady=10, fg='white', bg="black", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=25,
                    pady=10, fg='white', bg="black", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


