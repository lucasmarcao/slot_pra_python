from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("sera?")
window.geometry("400x400+500+200")
window.configure(bg="#808000")





greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
greeting.configure(background="#00ffff",justify="right")

botao = tk.Checkbutton(background="#800000",text="escolher",foreground="#ff00ff")
botao.pack()

botao2 = tk.Checkbutton(background="#800000",text="escolher",foreground="#ff00ff")
botao2.pack()

window.mainloop()
