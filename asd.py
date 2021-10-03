#!/usr/bin/env python3
#coding: utf-8
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox


def reverse_str():
    x = txt_edit.get(1.0, tk.END).strip()
    txt_edit.delete(1.0, tk.END)
    txt_edit.insert(tk.END, x[::-1])

def toupper_str():
    x = txt_edit.get(1.0, tk.END).strip()
    txt_edit.delete(1.0, tk.END)
    txt_edit.insert(tk.END, x.upper())

def tolower_str():
    x = txt_edit.get(1.0, tk.END).strip()
    txt_edit.delete(1.0, tk.END)
    txt_edit.insert(tk.END, x.lower())

def tostrformat_str():
    x = txt_edit.get(1.0, tk.END).strip()
    s = 'Minden karakter egy számjegy'
    s2 = 'Nem minden karakter számjegy'
    print(x.isdigit())
    if x.isdigit() == True:
        tk.messagebox.showinfo(title='Igaz', message=s)
    else:
        tk.messagebox.showinfo(title='Hamis', message=s2)
    

def to_txt():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Szövegfájlok", "*.txt"), 
                   ("Minden fájl",  "*.*")],
    )
    if not filepath:    # Amikor cancelt nyomsz a feljovo file exploreren, ures a filepath
        return
    with open(filepath, "w") as output_file:
        output_file.write(txt_edit.get(1.0, tk.END))


def open_file():
    filepath = askopenfilename(
        filetypes=[("Szövegfájlok", "*.txt"), 
                   ("Minden fájl",  "*.*")]
    )
    if not filepath:    # Amikor cancelt nyomsz a feljovo file exploreren, ures a filepath
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        txt_edit.insert(tk.END, input_file.read())


def w_counter():
    w = txt_in.get(1.0, tk.END).strip()     #szamolando szo
    x = txt_edit.get(1.0, tk.END).strip()   #szoveg
    s = 'A(z) "' + w + '"  ' + str(x.count(w)) + ' alkalommal fordul elő a szövegben.'
    tk.messagebox.showinfo(title='', message=s)


def w_remover():
    w = txt_in.get(1.0, tk.END).strip()     #torlendo szo
    x = txt_edit.get(1.0, tk.END).strip()   #szoveg
    res = tk.messagebox.askquestion('', 'Biztosan törölni szeretnéd a szövegből?')
    if res == 'yes':
        txt_edit.delete(1.0, tk.END)
        txt_edit.insert(1.0, x.replace(w,""))
    elif res == 'no':
        return
    else:
        tk.messagebox.showwarning('', 'Hiba!') 




##########################################################
##########################################################
##########################################################


window = tk.Tk()
window.title("Sztring Metódusok")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

txt_grid = tk.Frame(window, bd=2) #jobb oszlop
txt_label1 = tk.Label(txt_grid, text='Szöveg:')
txt_edit = tk.Text(txt_grid, height=15)
txt_label2 = tk.Label(txt_grid, text='Szó/kifejezés/szövegrészlet:')
txt_in = tk.Text(txt_grid, height=5)

txt_label1.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
txt_edit.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
txt_label2.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
txt_in.grid(row=3, column=0, sticky="ew", padx=5, pady=10)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2) #bal oszlop
b_open = tk.Button(fr_buttons, text="Megnyit", command=open_file)
b_save = tk.Button(fr_buttons, text="Mentés", command=to_txt)
b_rvrs = tk.Button(fr_buttons, text="Fordított", command=reverse_str)
b_upper = tk.Button(fr_buttons, text="Uppercase", command=toupper_str)
b_lower = tk.Button(fr_buttons, text="Lowercase", command=tolower_str)
b_szamvagynem = tk.Button(fr_buttons, text="Számjegy?", command=tostrformat_str)
b_search = tk.Button(fr_buttons, text="Szó törlése", command=w_remover)
b_count = tk.Button(fr_buttons, text="Szó megszámolása", command=w_counter)
b_clear = tk.Button(fr_buttons, text="Szövegmező ürítése", command=lambda: txt_edit.delete(1.0, tk.END))
b_exit = tk.Button(fr_buttons, text="Kilépés", command=window.destroy)

b_open.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
b_save.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
b_rvrs.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
b_upper.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
b_lower.grid(row=4, column=0, sticky="ew", padx=5, pady=10)
b_szamvagynem.grid(row=5, column=0, sticky="ew", padx=5, pady=10)
b_search.grid(row=6, column=0, sticky="ew", padx=5, pady=10)
b_count.grid(row=7, column=0, sticky="ew", padx=5, pady=10)
b_clear.grid(row=8, column=0, sticky="ew", padx=5, pady=50)
b_exit.grid(row=9, column=0, sticky="ew", padx=5, pady=10)


fr_buttons.grid(row=0, column=0, sticky="ns")
txt_grid.grid(row=0, column=1, sticky="nsew")

window.mainloop()