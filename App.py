#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import webbrowser    
try:
    import tkinter as tk
    from tkinter import *
   
except ImportError:
    import Tkinter as tk
    from Tkinter import tk
    
import os
import datetime

#import the texteditor file from the folder directory
import texteditor
from texteditor import *


#Build the parent window and lending it attributes
root = tk.Tk()
root.geometry('800x410')
root.title('All Under One')
root.resizable(width=False, height=False)
root.configure(background='grey')
#root.iconbitmap('/home/david/Desktop/MyProject/Untitled.ico')

#PLace the AU1 photo in the parent window
photo = PhotoImage(file='AU1.png')
phtlabel = Label(root, image=photo)
phtlabel.place(y=30, x=18)

#Import the tkcalender module and hold the error if module is not found
try:  
    import tkcalendar
    from tkcalendar import Calendar, DateEntry
    
except ImportError:
    calwin = Toplevel()
    calwin.title('Module Error!')
    calwin.resizable(width=False, height=False)
    calwin.geometry('330x70')
    callb = Label(calwin, text='Please install the tkcalendar module. :-)')
    callb.pack()
    def calwin_quit():
        calwin.destroy()
    calbtn = Button(calwin, text='Okay', command=calwin_quit)
    calbtn.pack(pady=3., padx=2)

fst_label = Label(root, text='Apps', background='#6a0819', foreground='white', 
                  width=100, height=1, font=('Calibri', 9, 'bold'))
fst_label.place(y=4, x=0)

expression = ""

#Build the calculator and place it under one function which
#is to be called in the calculator Button
def open_calc():
    
    def press(num): 
            global expression 
            expression = expression + str(num) 
            equation.set(expression) 

    #Function for the Equal sign Button	
    def equalpress(): 
            try:
                global expression 
                total = str(eval(expression)) 
                equation.set(total) 
                expression = "" 
            except: 
                equation.set(" SyntaxError!! ") 
                expression = ""

    #Function for the Clear Button            
    def clear(): 
            global expression 
            expression = "" 
            equation.set("")

    #Create the Calculator window
    if __name__ == "__main__": 
            gui = Toplevel() 
            gui.configure(background="grey") 
            gui.title("Calculator") 
            gui.geometry("337x150")
            gui.resizable(width=False, height=False)
            equation = StringVar() 
            expression_field = Entry(gui, textvariable=equation) 
            expression_field.grid(columnspan=4, ipadx=70) 
            equation.set('')
           
	    #Create and Place the Buttons in the calculator window
            button1 = Button(gui, text=' 1 ', fg='white', bg='black',
                             command=lambda: press(1), height=1, width=7, relief=FLAT)
            button1.grid(row=2, column=0) 

            button2 = Button(gui, text=' 2 ', fg='black', bg='grey',
                             command=lambda: press(2), height=1, width=7, relief=FLAT) 
            button2.grid(row=2, column=1) 

            button3 = Button(gui, text=' 3 ', fg='white', bg='black',
                             command=lambda: press(3), height=1, width=7, relief=FLAT) 
            button3.grid(row=2, column=2) 

            button4 = Button(gui, text=' 4 ', fg='black', bg='grey',
                             command=lambda: press(4), height=1, width=7, relief=FLAT) 
            button4.grid(row=3, column=0) 

            button5 = Button(gui, text=' 5 ', fg='white', bg='black',
                             command=lambda: press(5), height=1, width=7, relief=FLAT) 
            button5.grid(row=3, column=1) 

            button6 = Button(gui, text=' 6 ', fg='black', bg='grey',
                             command=lambda: press(6), height=1, width=7, relief=FLAT) 
            button6.grid(row=3, column=2) 

            button7 = Button(gui, text=' 7 ', fg='white', bg='black',
                             command=lambda: press(7), height=1, width=7, relief=FLAT) 
            button7.grid(row=4, column=0) 

            button8 = Button(gui, text=' 8 ', fg='black', bg='grey',
                             command=lambda: press(8), height=1, width=7, relief=FLAT) 
            button8.grid(row=4, column=1) 

            button9 = Button(gui, text=' 9 ', fg='white', bg='black',
                             command=lambda: press(9), height=1, width=7, relief=FLAT) 
            button9.grid(row=4, column=2) 

            button0 = Button(gui, text=' 0 ', fg='black', bg='grey',
                             command=lambda: press(0), height=1, width=7, relief=FLAT) 
            button0.grid(row=5, column=0) 

            plus = Button(gui, text=' + ', fg='black', bg='grey',
                          command=lambda: press("+"), height=1, width=7, relief=FLAT) 
            plus.grid(row=2, column=3) 

            minus = Button(gui, text=' - ', fg='white', bg='black',
                           command=lambda: press("-"), height=1, width=7, relief=FLAT) 
            minus.grid(row=3, column=3) 

            multiply = Button(gui, text=' * ', fg='black', bg='grey',
                              command=lambda: press("*"), height=1, width=7, relief=FLAT) 
            multiply.grid(row=4, column=3) 

            divide = Button(gui, text=' / ', fg='grey', bg='black',
                            command=lambda: press("/"), height=1, width=7, relief=FLAT) 
            divide.grid(row=5, column=3) 

            equal = Button(gui, text=' = ', fg='black', bg='grey',
                           command=equalpress, height=1, width=7, relief=FLAT) 
            equal.grid(row=5, column=2) 

            clear = Button(gui, text='Clear', fg='white', bg='black',
                           command=clear, height=1, width=7, relief=FLAT) 
            clear.grid(row=5, column='1') 

    def exit_btn():
            gui.destroy()
            
    exit = Button(gui, text='Quit', command=exit_btn,
                  height=1, width=7, background='black', foreground='white', relief=FLAT)
    exit.grid(row=5, column=3)
            
btn_calc = Button(root, text='Calculator', background='#6a0819', foreground='white',
                  relief=FLAT, width=10, height=2, activebackground='#1b3f55', activeforeground='white',
                  command=open_calc)

btn_calc.place(y=30, x=140)

#Build the tkcalender 

def open_calender():
    
    def quit_cal():
        calender_window.destroy()
        
    calender_window = tk.Toplevel(root)
    calender_window.title('Calender')
    calender_window.geometry('400x400')
    calender_window.resizable(width=False, height=False)

    today = datetime.date.today()

    cal = Calendar(calender_window, font="Arial 14", selectmode='day',
                   firstweekday='sunday', showweeknumbers=True,
                   locale='en_US',disabledforeground='red',cursor="hand1")
    
    cal.pack(fill="both", expand=True)
    cal_btn = Button(calender_window, text="ok", command=quit_cal)
    cal_btn.pack()
        
btn_calender = Button(root, text='Calender', activeforeground='white',
                      relief=FLAT, width=10, height=2, activebackground='#1b3f55',
                      background='#6a0819', foreground='white',
                      command=open_calender)

btn_calender.place(y=90, x=140)

#Create a function to test os name and open the File Browser
def open_files():
    
    if os.system('uname') == 'Windows':
        os.system('explorer')
    else:
        os.system('nautilus')
        
btn_files = Button(root, text='My Files', activeforeground='white',
                   relief=FLAT, width=10, height=2, activebackground='#1b3f55',
                   background='#6a0819', foreground='white',
                   command=open_files)

btn_files.place(y=150, x=140)

#Create a function to test os name and open the Internet Browser
def open_fire():
    if os.system('uname') == 'Windows':
        os.system('iexplorer')
    else:
        os.system('firefox')
                    
btn_firefox = Button(root, text='Browser', activeforeground='white',
                     relief=FLAT, width=10, height=2, activebackground='#1b3f55',
                     background='#6a0819', foreground='white',
                     command=open_fire)

btn_firefox.place(y=210, x=140)

#Create a function to test os name and open the Task Manger/System Monitor
def open_task_manager():
    if os.system('uname') == 'Windows':
        os.system('taskmgr')
    else:
        os.system('gnome-system-monitor')

        
btn_taskmanager = Button(root, text='Task Manager', activeforeground='white',
                         relief=FLAT, width=10, height=2, activebackground='#1b3f55',
                         background='#6a0819', foreground='white',
                         command=open_task_manager)

btn_taskmanager.place(y=270, x=140)


#Text editor code is in the texteditor.py file

#Call the text editor from the texteditor.py file
btn_text_editor = Button(root, text='Text Editor', activeforeground='white',
                         relief=FLAT, width=10, height=2, activebackground='#6a0819',
                         background='#1b3f55', foreground='white',
                         command=texteditor.txt)

btn_text_editor.place(y=30, x=540)

#Create a function to test os name and open the Command Line
def open_cli():
    if os.system('uname') == 'Windows':
        os.system("start /wait cmd /c {command}")
    else:
        os.system('gnome-terminal')

btn_terminal = Button(root, text='Command Line', activeforeground='white',
                      relief=FLAT, width=10, height=2, activebackground='#6a0819',
                      background='#1b3f55', foreground='white',
                      command=open_cli)

btn_terminal.place(y=90, x=540)

#Create a function to test os name and open the App Store
def open_app_store():
    if os.system('uname') == 'Windows':
        os.system('start ms-windows-store')
    else:
        os.system('gnome-software')

btn_app_store = Button(root, text='App Store', activeforeground='white',
                       relief=FLAT, width=10, height=2, activebackground='#6a0819', 
                       background='#1b3f55', foreground='white',
                       command=open_app_store)

btn_app_store.place(y=150, x=540)

#Create a function to test os name and open the System Music App
def open_music():
    if os.system('uname') == 'Windows':
        os.system('wmplayer')
    else:
        os.system('rhythmbox')

btn_music = Button(root, text='Music', activeforeground='white',
                   relief=FLAT, width=10, height=2, activebackground='#6a0819',
                   background='#1b3f55', foreground='white',
                   command=open_music)

btn_music.place(y=210, x=540)

#Create a function to test os name and open the Developer's README.txt File
def open_help():
    webbrowser.open('README.txt')


btn_help = Button(root, text='Help', activeforeground='white',
                  relief=FLAT, width=10, height=2, activebackground='#6a0819',
                  background='#1b3f55', foreground='white',
                  command=open_help)

btn_help.place(y=270, x=540)


    
dev_msg = Label(root,
                text="Copyright © mundiakaluson | 2019 | v1.0", font=('Calibri', 10, 'bold'), 
                background='grey', foreground='black')

dev_msg.place(y=390, x=3)
                  
"""

#My Gesture Toplevel() command will go here in version 1.2

########

#gesture_btn = Button(root, background='grey', foreground='white', relief=FLAT,
#                     text='Open Gestures Interface', height=1)
#gesture_btn.place(y=610, x=605)

"""
#Button for closing the root window
def quit_func():
    root.destroy()
    
quit_func = Button(root, activebackground='#6a0819', activeforeground='white',
                   background='#1b3f55', foreground='white', relief=FLAT,
                   text='Quit', command=quit_func)
quit_func.place(y=375, x=737)


mainloop()
 
