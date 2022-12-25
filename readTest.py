import pandas as pd
import pandas_gbq

pull = '''SELECT * FROM `chess-371023.chessPuzzles.puzzlesClean`'''

data = pd.read_gbq(query=pull,project_id='chess-371023')

print(data)