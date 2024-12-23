# Convert column of cells into list elements
# install openpyxl


from pathlib import Path
import pandas as pd

currfile_dir = Path(__file__).parent
file_path = currfile_dir / "compliment_kit.xlsx"
print(file_path)


#Insert complete path to the excel file and index of the worksheet
df = pd.read_excel(file_path, sheet_name=0)
# insert the name of the column as a string in brackets
list1 = list(df['term1'])
list2 = list(df['term2'])
list3 = list(df['term3'])
# remove nan from empty cells and any duplicates
list1 = [i for n, i in enumerate(list1) if i not in list1[:n] if isinstance(i, str)]
list2 = [i for n, i in enumerate(list2) if i not in list2[:n] if isinstance(i, str)]
list3 = [i for n, i in enumerate(list3) if i not in list3[:n] if isinstance(i, str)]
# output
print("term1 =", list1)
print("term2 =", list2)
print("term3 =", list3)
