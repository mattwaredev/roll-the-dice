# Roll the Dice
#### This Python script is simulating the six-sided dice. Player tracking and the announcement of the winner of each game and the option to choose how many sides (numbers) the dice will have will be available soon.

#### *Note: This script is currently under development and will be available to use soon.*
***
### GUI interface preview:

On the `Home page` you can see the window with one number. This number is the number on the dice. Also you can see two buttons. The first button "Roll the Dice" is to change the number above. The second button "Game Over" is to end the game. The app will ask you who won. You have to enter the name of the person who won. Then you have to press "OK". After this there will be a pop-up dialog that tell you the congratulation to winner:

<img width="179" height="271" alt="Screenshot 2026-07-06 at 15 00 07" src="https://github.com/user-attachments/assets/f163daaf-8e88-4a26-bc7f-d7dcbad7a2ce" />

This is the pop-up dialog using the `askstring` command to ask you who is the winner of the game:

<img width="179" height="271" alt="Screenshot 2026-07-06 at 15 00 35" src="https://github.com/user-attachments/assets/bae2c31d-2e32-41d4-a4f8-1af2f234ffec" />

This is the pop-up dialog using `showinfo` command to tell you the congratulation to winner:

<img width="179" height="271" alt="Screenshot 2026-07-06 at 15 01 30" src="https://github.com/user-attachments/assets/f0c6f849-8eba-4887-aa00-d2b68beb5e9a" />

There is a video preview of the app:

<img width="367" height="547" alt="Python" src="https://github.com/user-attachments/assets/8653339c-720f-4cc3-b4ff-c03d186e2189" />

***
### Top 5 interesting things in the Source Code:

#### 1. Aliasing When Importing Modules
The code uses so-called aliases (shortcuts) for imported modules and their parts, specifically `tk`, `sd`, and `mb`. This makes it easier for the programmer and shortens the subsequent calls to functions and methods from the `tkinter` library throughout the code.

```python
import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
```

#### 2. Simulation of a roll of a six-sided dice
To accurately simulate the roll of a standard dice, the code uses the `randint(1, 6)` function from the standard `random` library. This function guarantees that the generated number will always be an integer and will fall exactly within the range of 1 through 6, inclusive.

```python
new_number = random.randint(1, 6)
```

#### 3. Clearing and Overwriting the Displayed Value
To prevent two numbers from appearing next to each other when the dice is rolled again, the `change_number()` function uses the `delete(0, tk.END)` method, which first completely clears the `entry` array. Only then is a new number inserted into the first position (`0`) of the cleared array; this number must first be converted to a text string using the `str()` function.

```python
entry.delete(0,tk.END)
entry.insert(0, str(new_number))
```

#### 4. Using Pop-up Dialog Boxes
When the application exits (using the `end()` function), the code relies on two interactive pop-up windows. It uses the `askstring` command to prompt the user for text input (the winner's name) and then concatenates the variable into the thank-you message displayed in the `showinfo` information box.

```python
def end():
    player=sd.askstring('End of the Game', 'Who won?')
    mb.showinfo(title="Congratulations", message="Congratulations to "+player+" on his/her victory in this game!")
```

#### 5. Activating buttons using the `command` parameter
`tk.Button` graphical buttons communicate with the rest of the code using the `command` argument. This creates a direct link between the visual element and the execution of a specific function (`change_number` to roll the dice, `end` to exit) the moment the user clicks the button.

```python
button = tk.Button(window, text="Roll the Dice", font=("Helvetica", 16), command=change_number)
# ...
button = tk.Button(window, text="Game Over", font=("Helvetica", 16), command=end)
```
