import tkinter as tk

# Key-Value-Paare der Morsezeichen
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''                 # speichert die gegebenen Zeichen als Morsecode
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' ' # zwischen den eizelnen Zeichen kommt immer ein Freiraum
        else:   
            cipher += '  '                          # am Ende eines Wortes kommen zudem zwei weitere Leerzeichen dazu
    return cipher

REVERSE_DICT = {v:k for k, v in MORSE_CODE_DICT.items()} # mit v:k for k,v tauscht man einfach die Keys und die Values 

def decrypt(message):
    words = message.split('   ')    # einzelne Wörter werden daran erkaannt, dass drei Leerzeichend avor stehen
    decipher = []

    for word in words:
        letters = word.split(' ')   # Buchstaben lassen sich durch das Leerzeichen, zwischen ihnen, trennen
        decipher_word = ''          # sammelt alle Buchstaben bis ein Wort vollendet ist
        for letter in letters:
            if letter:              # ist true, wenn letter noch Morsecode für Buchstaben beinhaltet
                decipher_word += REVERSE_DICT[letter]
        decipher.append(decipher_word)

    return ' '.join(decipher)       # joint alle in decipher gesammelten Wörter zusammen, mit einen Leerzeichen zwischen ihnen

def encrypt_text():                 # Rest ist wichtig, damit die Funktionen von tk aufgerufen werden können
    text = entry.get()
    result = encrypt(text.upper())
    #label_result.config(text=result)

    label_result.delete(0, tk.END)
    label_result.insert(0, result)

def decrypt_text():
    text = entry.get()
    result = decrypt(text)
    #label_result.config(text=result)

    label_result.delete(0, tk.END)
    label_result.insert(0, result)

def copy_result(): # Copy-Button          
    text = label_result.get()
    window.clipboard_clear()
    window.clipboard_append(text)




window = tk.Tk()
window.title("Morse Code Converter")     # Titel
window.geometry('500x150')               # Größe des Windows

window.grid_columnconfigure(0, weight=1) # alles wird schön zentriert auch dynamisch
window.grid_columnconfigure(1, weight=1)

entry = tk.Entry(window, width=60)       # Eingabefeld - Größe etc.
entry.insert(0, "Text eingeben...")
entry.grid(row=0, column=0, columnspan=2, pady=10)

button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_text) # Encrypt-Button
button_encrypt.grid(row=1, column=0)

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_text) # Decrypt-Button
button_decrypt.grid(row=1, column=1)

button_copy = tk.Button(window, text="Copy", command=copy_result) # Copy-Button
button_copy.grid(row=3, column=1)

label_result = tk.Entry(window, width=60) # Rückgabefeld - Größe etc.
label_result.insert(0, "Ergebnis erscheint hier...")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop() # öffnet eine Dauerschleife für dieses Fenster und die möglichen Aktionen