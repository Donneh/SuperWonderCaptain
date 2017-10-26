#Brengt de speler naar het game-over scherm zodra hij 0 punten heeft.
def game_over_scherm():
    global file, label
    file = PhotoImage(file="gameover_scherm.gif")
    label = Label(root, image=file).place(x=0, y=0, relwidth=1, relheight=1)