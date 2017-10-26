from tkinter import *
from PIL import ImageTk, Image

# Maken van het Tkinter window
root = Tk()
entry_box = Entry()

# Het aantal punten waar elke speler mee start
punten = 0

canvas = Canvas(root, height=0, width=500)

achtergrond = PhotoImage(file="beginscherm.gif")

label_achtergrond = Label(root, image=achtergrond)
label_achtergrond.place(x=1, y=0, relwidth=1, relheight=0.85)

button = Button(root, font=("arial", 25, "bold"), fg="yellow2", text="Ben je er klaar voor?", bg="hot pink",
                command=tweede_scherm)
button.pack(side="bottom")

root.title("SuperWonderCaptain")
root.geometry("650x500")
root.resizable(0, 0)

canvas.pack()

root.mainloop()
