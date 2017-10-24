import datetime
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import os
import sys


def inputHighscore():
    name = input("What is your name? ")
    score = input("What is your score? ")
    time = str(datetime.datetime.now())
    string = ','.join([name, score, time])
    file = open("highscore.txt", "a")
    file.write(string + '\n')
    file.close()


def getHighscores():
    dict = {}
    with open('highscore.txt', 'r') as file:
        index = 0
        for line in file:
            parts = line.split(',')
            dict[index] = {}
            dict[index]['name'] = parts[0]
            dict[index]['score'] = parts[1]
            dict[index]['datetime'] = parts[2]
            index += 1

    return dict


root = Tk()
frame = Frame(root, width=200, height=100)
tree = ttk.Treeview(frame)

tree = Treeview(root, selectmode="extended", columns=(0, 1, 2), show="headings")
tree.column(0, minwidth=0, width=100, stretch=NO)
tree.heading(0, text="Name")
tree.column(1, minwidth=0, width=200, stretch=NO)
tree.heading(1, text="Score")
tree.column(2, minwidth=0, width=300, stretch=NO)
tree.heading(2, text="Datetime")

for key, user in getHighscores().items():
    tree.insert("", 0, user['name'], values=(user['name'], user['score'], user['datetime']))

tree.grid(column=3, row=1)
tree.pack(expand=YES, fill=BOTH)
frame.pack()
mainloop()
