from tkinter import *
import tkinter.ttk as ttk
from googletrans import Translator
from tkinter import messagebox
from PIL import Image, ImageTk

win = Tk()
win.title("Translator | HackersBrain")
win.geometry("660x310")
win.config(background="#ffffff")
win.minsize(width=660, height=310)
win.maxsize(width=660, height=310)


def translate():
    word = entry1.get()
    if word == '':
        messagebox.showinfo(title="Error Occurred.", message="Please Enter A Word.")
    else:
        translator = Translator(service_urls=['translate.google.com'])
        translation1 = translator.translate(word, dest='spanish')
        messagebox.showinfo(title="Translated in Spanish", message=f"Translated in Spanish : \n{translation1.text}")


banner = Image.open("google_translate.png")
render = ImageTk.PhotoImage(banner)
ban = ttk.Label(win, image=render, background="#ffffff")
ban.grid(row=0, column=1, padx=5, pady=35)

text = ttk.Label(win, text="Enter text or word : ", background="#ffffff")
text.grid(row=1, column=0, padx=8)

entry1 = ttk.Entry(win, width=40)
entry1.grid(row=1, column=1, padx=1)

author = ttk.Label(win, text="HackersBrain", background="#ffffff")
author.grid(row=1, column=2)

button = ttk.Button(win, text="Translate", command=translate)
button.grid(row=2, column=1, padx=3, pady=25)

win.mainloop()
