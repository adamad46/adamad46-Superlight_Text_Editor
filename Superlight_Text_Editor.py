from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import threading
import json
import subprocess
import sys
from win32api import GetSystemMetrics
from tkinter import ttk


root = tk.Tk()
root.title("Adam's text editor")
root.config(bg='#181915')


if os.path.exists('config.txt') == False:
    file1 = open('config.txt', 'x')
    file1.close()

file2 = open('config.txt', 'r+')






def save_file():
    global file
    file = open(str(selected_file), 'r+')
    file.truncate(0)
    file.write(str(text_box.get("1.0","end")))
    file.close()

def main_run():
    python = f'python "{selected_file}"'
    os.system(python)
def run():

    x = threading.Thread(target=main_run)
    x.start()

def choose_file_and_open():

    try:
        ask_open = filedialog.askopenfile(initialdir=os.getcwd())
        global selected_file
        selected_file = (ask_open.name)
        global file
        file = open(str(selected_file), 'r+')

        text_box.delete(1.0, END)
        text_box.insert(1.0, file.read())
        choose_file.pack_forget()
        save_button.pack(side=LEFT,padx=8, pady=12)
        choose_file.pack(side=LEFT, padx=8, pady=12)
        clear_button.pack(side=RIGHT, padx=8, pady=12)
        delete_file_button.pack(side=RIGHT, padx=8, pady=12)
        if '.py' in str(selected_file):
            run_py_button.pack_forget()
            run_py_button.pack(side=LEFT, padx=8, pady=12)
        else:
            run_py_button.pack_forget()
    except:
        pass









def clear():
    text_box.delete(1.0, END)

def delete():
    ask = messagebox.askyesno('WARNING', (f'Would you like to delete this file:\n {selected_file}'))
    if ask == True:
        file.close()
        os.remove(selected_file)
        clear()

    elif ask == False:
        pass







def settings_main():
    global textsize_entry
    global error_textsize
    master = Toplevel(root)
    master.config(bg='#181915')
    master.geometry(f'{int(GetSystemMetrics(0)/1.9)}x{int(GetSystemMetrics(1)/1.9)}')
    textsize_label = Label(master, text='text size:', bg = '#181915', fg='#F8F8F2', font='verdana 17')
    textsize_label.pack(side=TOP)
    textsize_entry = Entry(master, font='verdana 14', bg='grey')
    textsize_entry.pack(side=TOP)
    submit_textsize = Button(master, text='submit', bg='#181915', fg='#F8F8F2',font='verdana 14', command = font_submit)
    submit_textsize.pack(side=TOP)
    error_textsize = Label(master, bg='#181915', fg='red', text='error', font='verdana 20')




    ###########functions^##############
    ###################################
    ###################################
choose_file = Button(root, text='choose file', command=choose_file_and_open,bg='#20211C', font='verdana 13',padx=10,pady=10,fg='#c9c9c5')
choose_file.pack(side=BOTTOM, padx=8, pady=12)


clear_button = Button(root, text='clear', command=clear,bg='#20211C', font='verdana 13',padx=10,pady=10,fg='#c9c9c5')


delete_file_button = Button(root, text='delete file', command=delete,bg='#20211C',fg='#c9c9c5', font='verdana 13',padx=10,pady=10)



save_button = Button(root, text='save', command=save_file,bg='#20211C',fg='#c9c9c5', font='verdana 13',padx=10,pady=10)

run_py_button = Button(root, text='▶', command=run, font='verdana 13',padx=10,pady=10,bg='#20211C',fg='#F8F8F2')

text_box = Text(root,bg='#282923',fg='#F8F8F2', font='verdana 13',highlightthickness=0, padx=6, pady=6, height=30, width=140, wrap='none')
text_box.pack(padx=8, pady=12)

        #####################################





root.mainloop()
