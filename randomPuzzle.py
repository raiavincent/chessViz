import webbrowser
import pandas as pd
import pandas_gbq
import random
import requests

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

getPuzzle()