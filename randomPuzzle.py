import webbrowser
import pandas as pd
import pandas_gbq
import random
import requests
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

pull = '''SELECT * FROM `chess-371023.chessPuzzles.puzzlesClean`'''

data = pd.read_gbq(query=pull,project_id='chess-371023')

puzzleList = list(data['puzzleID'])

def getPuzzle():

    randomPuzzle = random.choice(puzzleList)

    puzzle = randomPuzzle[1:]

    puzzleLink = ('https://lichess.org/training/' + puzzle)

    r = requests.get(puzzleLink)

    webbrowser.open(puzzleLink)

    # need to figure out 404 handling, afraid of continuous recursion
    # if r.status_code == 404:
    #     getPuzzle
    # else:
    #     webbrowser.open(puzzleLink)

    print(data.loc[data['puzzleID'] == randomPuzzle])

    canvas1.insert(data.loc[data['puzzleID'] == randomPuzzle])

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

# def exit_application():
#     msg_boxRun = tk.messagebox.askquestion('Puzzle?'
#                                         icon='warning')
#     if msg_boxRun == 'yes':
#         root.destroy()
#     else:
#         tk.messagebox.showinfo('Return', 'You will now return to the application screen')

button1 = tk.Button(root, text='Puzzle?', command=getPuzzle, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()

# getPuzzle()