import tkinter as tk
from tkinter import font

root = tk.Tk() # Hauptfenster der Anwendung erstellen
root.title("Einfacher Taschenrechner") # Titel 
root.geometry("500x500") # Größe des Fensters
root.minsize(300,300) # minimale Größe des Fensters, falls es verkleinert wird
font_general = font.Font(size = 20, family = "Arial") 
# Eingabefeld und Buttons sollen selbe Schriftart haben

entry = tk.Entry(root, width = 30, borderwidth = 20, font = font_general) 
# das Eingabefeld des Teschenrechners 
entry.grid(row = 0, column = 0, columnspan = 4, sticky = "nswe") 
# die Stelle im Fenster an der das Eingabefeld angelegt werden soll und wie groß es 
# sein soll (columnspan = 4)

buttons = [
    "7", "8", "9", "/", # anzuzeigende Buttons des Taschenrechners in ihrer Reihenfolge
    "4", "5", "6", "*",
    "1", "2", "3", "+",
    "0", ".", "-", "="
]

row_val = 1 # Buttons sollen in Row 1 starten, da in Row 0 das Eingabefeld ist
col_val = 0 # Spalte wird durchs Eingabefeld nicht beeinflusst, daher 0

def calculate():
    try:
        expression = entry.get() # es wird das geholt, was im Eingabefeld steht
        result = eval(expression) # die eval Funktion rechtnet die Eingabe aus 
                                  # (kann aber beispielsweise auch Pythoncode im Terminal ausführen !!!)
        entry.delete(0, tk.END) # das Eingabefeld wird geleert
        entry.insert(tk.END, str(result)) # abschließend wird das Ergebnis der Eingabe dort dargestellt
    except (SyntaxError, TypeError, NameError, ZeroDivisionError):
        entry.delete(0, tk.END) # falls die Eingabe fehlerhaft ist, wird die Eingabe gelöscht
        entry.insert(tk.END, "Error") # danach wird dort Error ausgegeben

def clear():
    entry.delete(0, tk.END) # Funktion zum Löschen des vollständigen Inhalts des Eingabefeldes

for button in buttons:
    command = lambda b = button: calculate() if b == "=" else entry.insert(tk.END, b)
    # eine Callback-Funktion definieren, die entweder das Eingegebene ausrechnet, wenn der 
    # "=" Button gedrückt wurde oder das Zeichen des Buttons ebenfalls zum Eingabefeld hinzufügt
    # b = button sorgt dafür, dass der aktuelle Button als Standardargument gespeichert 
    # und bearbeitet wird
    tk.Button(root, text = button, font = font_general, command = command).grid(row = row_val, column = col_val, sticky = "nswe")
    # die Art und Weise wie die Buttons erstellt werden
    col_val += 1 # nach jedem Botton wandert man ein Column weiter und wenn man bei 4 
                 # angekommen ist, geht man eine Row tiefer und fängt wieder bei Column 0 an
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text = "Clear", font = font_general, command = clear).grid(row = row_val, column = 0, columnspan = 4, sticky = "nswe")
# ganz am Ende wird noch der Clear-Button angefügt, der wie das Eingabefeld über alle Columns reicht

for column in range(4):
    root.columnconfigure(column, weight = 1)
# steuert die Verteilung zusätzlichen Platzes (z.B. bei größerem Fenster)
# das Gewicht ist gleich, damit sie sich bei Größenänderungen gleichmäßig an das Fenster anpassen

for row in range(5):
    root.rowconfigure(row, weight = 1) 
# steuert die Verteilung zusätzlichen Platzes (z.B. bei größerem Fenster)
# das Gewicht ist gleich, damit sie sich bei Größenänderungen gleichmäßig an das Fenster anpassen

root.mainloop() # startet die Ereignisschleife und hält das Fenster geöffnet, 
                # bis es geschlossen wird