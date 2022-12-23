# need credentials
# need to download libraries

import pandas as pd
from janitor import xlsx_table
import pandas_gbq
from tableSchema import table_schema
import os
import datetime
from puzzleCredentials import table_id
from puzzleCredentials import project_id

filePath = r"C:\Users\vince\OneDrive\Chess\training - v2.xlsx"

print('Locating data.')

puzzleHistory = xlsx_table(filePath, sheetname='table', table='puzzleScoring')

print('Data located.')

print(puzzleHistory)

pandas_gbq.to_gbq(
    puzzleHistory, table_id, project_id=project_id, if_exists='append',
    table_schema=table_schema)

print('Data uploaded.')
    