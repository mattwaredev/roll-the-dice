import tkinter as tk
from tkinter import messagebox as mb
import random

minimum_number = 1
maximum_number = 6
roll_history = []


def change_number():
    new_number = random.randint(minimum_number, maximum_number)
    entry.delete(0, tk.END)
    entry.insert(0, str(new_number))
    roll_history.insert(0, new_number)
    del roll_history[5:]
    history_listbox.delete(0, tk.END)
    for number in roll_history:
        history_listbox.insert(tk.END, number)


def numbers_settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("Numbers settings")
    settings_window.geometry("360x330")
    settings_window.resizable(False, False)

    sides = (
        ("Four-sided", 4),
        ("Six-sided", 6),
        ("Eight-sided", 8),
        ("Ten-sided", 10),
        ("Twelve-sided", 12),
        ("Twenty-sided", 20),
    )

    minimum_entry = tk.Entry(settings_window, justify="center", width=10)
    maximum_entry = tk.Entry(settings_window, justify="center", width=10)

    def show_range(minimum, maximum):
        minimum_entry.delete(0, tk.END)
        minimum_entry.insert(0, str(minimum))
        maximum_entry.delete(0, tk.END)
        maximum_entry.insert(0, str(maximum))

    for index, (label, number_of_sides) in enumerate(sides):
        tk.Button(
            settings_window,
            text=label,
            command=lambda sides=number_of_sides: show_range(1, sides),
        ).grid(row=index // 2, column=index % 2, sticky="ew", padx=8, pady=5)

    fields_row = len(sides) // 2
    settings_window.grid_columnconfigure(0, weight=1)
    settings_window.grid_columnconfigure(1, weight=1)

    tk.Label(settings_window, text="Maximum").grid(
        row=fields_row, column=0, padx=8, pady=(16, 2)
    )
    maximum_entry.grid(row=fields_row + 1, column=0, padx=8, pady=2)
    tk.Label(settings_window, text="Minimum").grid(
        row=fields_row, column=1, padx=8, pady=(16, 2)
    )
    minimum_entry.grid(row=fields_row + 1, column=1, padx=8, pady=2)

    def apply_range():
        try:
            minimum = int(minimum_entry.get())
            maximum = int(maximum_entry.get())
        except ValueError:
            mb.showerror("Invalid range", "Enter whole numbers for the minimum and maximum.")
            return

        if minimum > 999 or maximum > 999:
            mb.showerror("Invalid range", "The minimum and maximum must not exceed 999.")
            return

        if minimum > maximum:
            mb.showerror("Invalid range", "The minimum must not be greater than the maximum.")
            return

        global minimum_number, maximum_number
        minimum_number = minimum
        maximum_number = maximum
        settings_window.destroy()

    show_range(minimum_number, maximum_number)
    tk.Button(settings_window, text="Apply", command=apply_range).grid(
        row=fields_row + 2, column=0, columnspan=2, pady=(12, 8)
    )

window = tk.Tk()
window.title("Roll the Dice")

main_frame = tk.Frame(window)
main_frame.pack(padx=20, pady=20)

entry = tk.Entry(main_frame, font=("Helvetica", 300), justify='center', width=4)
initial_number = random.randint(minimum_number, maximum_number)
entry.insert(0, str(initial_number))
entry.grid(row=0, column=0, padx=(0, 20))

history_frame = tk.Frame(main_frame)
history_frame.grid(row=0, column=1, sticky="n")
tk.Label(history_frame, text="Last 5 rolls").pack(pady=(0, 5))
history_listbox = tk.Listbox(history_frame, height=5, width=12, justify="center")
history_listbox.pack()
roll_history.append(initial_number)
history_listbox.insert(tk.END, initial_number)

button = tk.Button(window, text="Roll the Dice", command=change_number)
button.pack(pady=10)

button = tk.Button(window, text="Numbers settings", command=numbers_settings)
button.pack(pady=10)

window.mainloop()