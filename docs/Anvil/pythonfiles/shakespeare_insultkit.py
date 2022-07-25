import pandas as pd
# import numpy as np

#Insert complete path to the excel file and index of the worksheet
df = pd.read_excel("insultkit.xlsx", sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['Insult1']) 
list2 = list(df['Insult2'])
list3 = list(df['Insult3'])
print(list1)
print(list2)
print(list3)