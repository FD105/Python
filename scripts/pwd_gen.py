import secrets
import string
import tkinter as tk

root = tk.Tk() # Angaben zum Fenster
root.geometry("400x200")
root.title("Pwd-Generator")

def generate_password(): # es soll aus allen Buchstaben, Zahlen und Sonderzeichen gewählt werden
    usable = (
        string.ascii_letters + 
        string.digits + 
        string.punctuation
    )
    password = "".join(secrets.choice(usable) 
                       for _ in range(16)) # 16 ausgewählte Zeichen werden zufällig gewählt
    entry.delete(0, tk.END) # das was bisher im Eingabefeld steht, wird gelöscht
    entry.insert(0, password) # das neu erstellte Passwort wird dort angezeigt

def copy_to_clipboard():
    root.clipboard_clear() # Löscht bisherigen Inhalt der Zwischenablage
    root.clipboard_append(entry.get()) # liest den Text aus dem Eingabefeld 
                                       # aus und fügt ihn der Zwischenablage hinzu

tk.Button(root, text = "New Password", command = generate_password).pack(pady = 20)
# erstellt einen Button in diesem Fenster, welcher die Funktion "generate_password" aufruft
entry = tk.Entry(root, font = ("Arial", 24), justify = "center")
entry.pack(pady = 10)
# speichert das Eingabefeld in einer Variable, damit man mit entry.get() darauf zugreifen kann
tk.Button(root, text = "Copy", command = copy_to_clipboard).pack(pady = 10)
# erstellt einen weiteren Button, welcher die "copy_to_clipboard"-Funktion aufruft

root.mainloop() # startet die Ereignisschleife und hält das Fenster geöffnet, 
                # bis es geschlossen wird