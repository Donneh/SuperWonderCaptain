from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("SuperWonderCaptain")
entry_box = Entry()


def volgend_scherm():
    global file
    global label
    global canvas
    global naam
    global entry_box
    root.geometry("650x500")
    root.resizable(0, 0)
    canvas = Canvas(root, height=650, width=500)
    canvas.pack()
    file = PhotoImage(file="deadpool.resized.gif")
    label = Label(root, image=file)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    label2 = Label(root, font=("arial", 17, "bold"), bg="gray9", fg="white", text="Punten: " + str(punten))
    label2.place(x=10, y=10)

    naamVraag = Label(root, text="Naam:", font=("arial", 12, "bold"), bg="gray9", fg="red").place(x=5, y=115)
    entry_box = Entry(root, width=18, bg="dark slate gray")
    entry_box.place(x=60, y=118)
    start = Button(root, text="Start", width=5, height=1, command=doeHet).place(x=61, y=137)



def doeHet():
    global entry_box
    if entry_box.get() is "":
        print("Voer een geldige naam in.")
    else:
        print("Succes met de uitdaging, " + str(entry_box.get().capitalize()) + "!")
        canvas = Canvas(root, height=0, width=500)
        file2 = PhotoImage(file="logo6.gif")
        label2 = Label(root, image=file2)
        label2.place(x=1, y=0, relwidth=1, relheight=0.85)
        canvas.pack()
        root.geometry("500x375")
        root.resizable(0, 0)
        root.mainloop()


punten = 0;

canvas = Canvas(root, height=0, width = 500)

file = PhotoImage(file="logo6.gif")

label = Label(root, image=file)
label.place(x=1, y=0, relwidth=1, relheight=0.85)
canvas.pack()

button = Button(root, font=("arial", 25, "bold"), fg="yellow2", text="Ben je er klaar voor?", bg="hot pink", command=volgend_scherm)
button.pack(side="bottom")

root.geometry("500x450")
root.resizable(0, 0)
root.mainloop()
