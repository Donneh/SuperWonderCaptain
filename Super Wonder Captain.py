from tkinter import *
from PIL import ImageTk, Image

# Deze functie brengt de speler naar het volgende scherm, achtergrond en de startknop
def tweede_scherm():
    global achtergrond, label_achtergrond, canvas, naam, entry_box
    canvas = Canvas(root, height=650, width=500).pack()
    achtergrond = PhotoImage(file="tweede_achtergrond.gif")
    label_achtergrond = Label(root, image=achtergrond)
    label_achtergrond.place(x=0, y=0, relwidth=1, relheight=1)

# Vragen naar de naam van de speler en creëren van de start knop
    naam_vraag = Label(root, text="Naam:", font=("arial", 17, "bold"), bg="gray9", fg="red").place(x=4, y=117)
    entry_box = Entry(root, width=18, bg="dark slate gray")
    entry_box.place(x=60, y=118)
    start_button = Button(root, text="Start", width=5, height=1, command=derde_scherm).place(x=60, y=143)

# Creatie van het derde scherm en van de opties waar de speler uit kan kiezen
def derde_scherm():
    global entry_box, achtergrond, label_achtergrond

# Als de speler een ongeldige naam invoert, start het spel niet
    if entry_box.get() is "":
        print("Voer een geldige naam in.")

# Creatie van het starten van het spel en het spelen
    else:
        print("Succes met de uitdaging, " + str(entry_box.get().capitalize()) + "!")
        achtergrond= PhotoImage(file="derde_achtergrond.gif")
        label_achtergrond = Label(root, image=achtergrond).place(x=0, y=0, relwidth=1, relheight=1)
        punten_label= Label(root, font=("arial", 15, "bold"),bg= "white", text="Punten: "+ str(punten)).place(x=10, y=150)

# Creatie van de opties waar de speler uit kan kiezen (meerkeuze)
        optie1 = Radiobutton(label_achtergrond, text="Optie 1", value=1).place(x=20, y=225)
        optie2 = Radiobutton(label_achtergrond, text="Optie 2", value=2).place(x=20, y=250)
        optie3 = Radiobutton(label_achtergrond, text="Optie 3", value=3).place(x=20, y=275)
        optie4 = Radiobutton(label_achtergrond, text="Optie 4", value=4).place(x=20, y=300)
        optie5 = Radiobutton(label_achtergrond, text="Optie 5", value=5).place(x=20, y=325)
        optie6 = Radiobutton(label_achtergrond, text="Optie 6", value=6).place(x=20, y=350)
        optie7 = Radiobutton(label_achtergrond, text="Optie 7", value=7).place(x=20, y=375)
        optie8 = Radiobutton(label_achtergrond, text="Optie 8", value=8).place(x=20, y=400)
        optie9 = Radiobutton(label_achtergrond, text="Optie 9", value=9).place(x=20, y=425)
        optie10 = Radiobutton(label_achtergrond, text="Optie 10", value=10).place(x=20, y=450)




# Maken van het Tkinter window
root = Tk()
entry_box = Entry()

# Het aantal punten waar elke speler mee start
punten = 0;

canvas = Canvas(root, height=0, width = 500)

achtergrond = PhotoImage(file="beginscherm.gif")

label_achtergrond = Label(root, image=achtergrond)
label_achtergrond.place(x=1, y=0, relwidth=1, relheight=0.85)


button = Button(root, font=("arial", 25, "bold"), fg="yellow2", text="Ben je er klaar voor?", bg="hot pink", command=tweede_scherm)
button.pack(side="bottom")

root.title("SuperWonderCaptain")
root.geometry("650x500")
root.resizable(0, 0)

canvas.pack()

root.mainloop()
