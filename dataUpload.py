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
import warnings

# data does not live in the same location as my code, need to direct the code to that location
filePath = r"C:\Users\vince\OneDrive\Chess\training - v2.xlsx"

print('Locating data.')

# using the xlsx_table function from pyjanitor to extract my data
puzzleHistory = xlsx_table(filePath, sheetname='table', table='puzzleScoring')

print('Data located.')

# a package has a deprecation warning I would like to temporarily ignore
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# housing data in BigQuery, using pandas_gbq to facilitate the uploads
pandas_gbq.to_gbq(
    puzzleHistory, table_id, project_id=project_id, if_exists='replace',
    table_schema=table_schema)

# just creating an output to show the code is complete
print('Data uploaded.')
    