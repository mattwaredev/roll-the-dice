import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import random

def change_number():
    new_number = random.randint(1, 6)
    entry.delete(0, tk.END)
    entry.insert(0, str(new_number))

def end():
    player=sd.askstring('End of the Game', 'Who won?')
    mb.showinfo(title="Congratulations", message="Congratulations to "+player+" on his/her victory in this game!")

window = tk.Tk()
window.title("Roll the Dice")

entry = tk.Entry(window, font=("Helvetica", 300), justify='center', width=2)
entry.insert(0, str(random.randint(1, 6)))
entry.pack(pady=20)

button = tk.Button(window, text="Roll the Dice", font=("Helvetica", 16), command=change_number)
button.pack(pady=10)

button = tk.Button(window, text="End of the Game", font=("Helvetica", 16), command=end)
button.pack(pady=10)

window.mainloop()