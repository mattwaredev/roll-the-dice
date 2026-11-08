# Roll the Dice
#### This Python script is simulating the six-sided dice. Player tracking and the announcement of the winner of each game and the option to choose how many sides (numbers) the dice will have will be available soon.

***
### GUI interface preview:

On the home page, there is a large field displaying a number. This number is the result of the most recent dice roll. To the right of this field is a smaller field that displays the last 5 rolls. Click the `Roll the Dice` button to roll again. The `Numbers settings` button opens a separate window where you can set the range of numbers to be rolled:

<img width="481" height="318" alt="home" src="https://github.com/user-attachments/assets/c221f502-8427-439e-9bb1-54039722e9a2" />

When you click the `Numbers settings` button, this window opens:

<img width="472" height="474" alt="numbers" src="https://github.com/user-attachments/assets/c89254af-1a51-4d7b-8518-78f71d115933" />

***
### Top 5 interesting details in the Source Code:

#### 1. The dice range is configurable
Every roll uses the current minimum and maximum, so the app can simulate more than a standard six-sided die.

```python
minimum_number = 1
maximum_number = 6

def change_number():
    new_number = random.randint(minimum_number, maximum_number)
```

#### 2. It includes presets for several polyhedral dice
The settings window offers dice with 4, 6, 8, 10, 12, or 20 sides.

```python
sides = (
    ("Four-sided", 4),
    ("Six-sided", 6),
    ("Eight-sided", 8),
    ("Ten-sided", 10),
    ("Twelve-sided", 12),
    ("Twenty-sided", 20),
)
```

#### 3. The preset buttons avoid a common loop-lambda pitfall
`sides=number_of_sides` captures each button’s value when it is created, so every preset selects the intended number of sides.


```python
command=lambda sides=number_of_sides: show_range(1, sides),
```

#### 4. The roll history is newest-first and limited to five entries
New results are added at the beginning, and older entries beyond the fifth are removed.

```python
roll_history.insert(0, new_number)
del roll_history[5:]
```

#### 5. The initial roll appears in both the entry and the history
The app starts with a random result and immediately records it, so the history is populated before the first button click.


```python
initial_number = random.randint(minimum_number, maximum_number)
entry.insert(0, str(initial_number))

roll_history.append(initial_number)
history_listbox.insert(tk.END, initial_number)
```
