from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Body-Mass-Index")
root.geometry("300x200+800+400")
root.resizable(False, False)

def ergebnis_frau():
    try:
        a = float(ent_gewicht.get().replace(",", "."))
        b = float(ent_groesse.get().replace(",", "."))

        if a > 0 and b > 0:
            label_ausgabe2["text"] = ""
            c = a / ((b / 100) ** 2)
            label_ausgabe["text"] = c.__round__(2)
        else:
            label_ausgabe["text"] = "Ungültige Eingabe"

    except ValueError:
        label_ausgabe["text"] = "Bitte die Zahlen eingeben"

    if c < 17:
        label_ausgabe2["text"] = "Untergewicht"
        label_ausgabe2["background"] = "yellow"
    elif c > 18 and c < 25:
        label_ausgabe2["text"] = "Normalgewicht"
        label_ausgabe2["background"] = "green"
    elif c > 25 and c < 30:
        label_ausgabe2["text"] = "Übergewich"
        label_ausgabe2["background"] = "yellow"
    elif c > 30 and c < 35:
        label_ausgabe2["text"] = "Übergeicht Stuffe 1"
        label_ausgabe2["background"] = "red"
    elif c > 35 and c < 40:
        label_ausgabe2["text"] = "Übergeicht Stuffe 2"
        label_ausgabe2["background"] = "red"
    elif c > 40:
        label_ausgabe2["text"] = "!!! Übergeicht Stuffe 3 !!!"
        label_ausgabe2["background"] = "red"


label_gewicht = ttk.Label(root, text="Gewicht", font="Arial 10 bold")
label_gewicht.place(relx=0.22, rely=0.01)
label_groesse = ttk.Label(root, text="Größe", font="Arial 10 bold")
label_groesse.place(relx=0.60, rely=0.01)
label_ergebnis = ttk.Label(root, text="Ergebnis", font="Arial 10 bold")
label_ergebnis.place(relx=0.42, rely=0.3)
label_ausgabe = ttk.Label(root, font="Arial 10 bold", width=37, anchor=CENTER)
label_ausgabe.place(relx=0.05, rely=0.45)
label_ausgabe2 = ttk.Label(root, font="Arial 10 bold", width=37, anchor=CENTER)
label_ausgabe2.place(relx=0.05, rely=0.58)


ent_gewicht = ttk.Entry(width=8, justify="center")
ent_gewicht.place(relx=0.23, rely=0.13)
ent_groesse= ttk.Entry(width=8, justify="center")
ent_groesse.place(relx=0.59, rely=0.13)

btn_ausführen = ttk.Button(text="Ausführen", command=ergebnis_frau)
btn_ausführen.place(relx=0.675, rely=0.75)

root.mainloop()