from tkinter import *
from PIL import ImageTk, Image

#Brengt de speler naar het game-over scherm zodra hij 0 punten heeft.
def game_over_scherm():
    global achtergrond, label_achtergrond
    file = PhotoImage(file="gameover_scherm.gif")
    label = Label(root, image=file).place(x=0, y=0, relwidth=1, relheight=1)

# Deze functie laat een pop up zien waarin de speler succes toegewenst wordt
def succes_PopUp():
    succes_tekst = "Succes met de uitdaging, " + str(entry_box.get().capitalize()) + "!"
    toplevel = Toplevel()
    succes_popup_label = Label(toplevel, text=succes_tekst, height=5, width=50).pack()
    sluit_popup = Button(toplevel, text="Dankjewel!",command= toplevel.destroy).place(x=175, y=59)
    toplevel.resizable(0,0)

# Deze functie geeft een foutmelding aan de gebruiker wanneer die een ongeldige naam invoert
def ongeldige_naam_PopUp():
    ongeldige_naam= "Voer een geldige naam in, een naam moet minimaal 1 karakter bevatten en maximaal 15."
    toplevel= Toplevel()
    ongeldige_naam_label= Label(toplevel, text=ongeldige_naam, height= 5, width= 65).pack()
    sluit_PopUp= Button(toplevel, text="Begrepen.", command= toplevel.destroy).place(x=250, y=59)
    toplevel.resizable(0,0)




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
    entry_box.place(x=60, y=116)
    start_button = Button(root, text="Start", width=5, height=1, command=derde_scherm).place(x=61, y=150)
    quit = Button(root, font=("arial", 10, "bold"), bg="gray9", fg="red", text="Quit", width=15, command=root.destroy).place(x=533, y=479)

# Creatie van het derde scherm en van de opties waar de speler uit kan kiezen
def derde_scherm():
    global entry_box, achtergrond, label_achtergrond

# Als de speler een ongeldige naam invoert, start het spel niet
    if entry_box.get() is "" or len(entry_box.get()) > 15:
        ongeldige_naam_PopUp()

# Creatie van het starten van het spel en het spelen
    else:
        succes_PopUp()
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
# Creatie van de 'Hint Button' die de speler een hint geeft ten koste van 3 punten
        hint_button= Button(label_achtergrond, font=("arial", 9, "bold"), fg="OrangeRed3",text="HINT(-3 punten)").place(x=462, y=250)
# Creatie van de button die de keuze van de speler bevestigt
        ok_button= Button(label_achtergrond, font=("arial", 9, "bold"), text="BEVESTIGEN").place(x=150, y=450)
        quit = Button(root, font=("arial", 10, "bold"), bg="gray9", fg="red", text="Quit", width=15, command=root.destroy).place(x=533, y=472)




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

# Creatie van de button om de applicatie af te sluiten; "quit"
quit = Button(root, font=("arial", 10, "bold"), bg="red", fg="red", text="Quit", width=15, command=root.destroy).place(x=533, y=479)

button.pack(side="bottom")

root.title("SuperWonderCaptain")
root.geometry("650x500")
root.resizable(0, 0)

canvas.pack()

root.mainloop()
