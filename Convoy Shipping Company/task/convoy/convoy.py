import pandas as pd
import os

print("Input file name")
file_name = input()
file_name_parts = os.path.splitext(file_name)
file_name_csv = file_name_parts[0] + ".csv"
my_df = pd.read_excel(file_name, sheet_name='Vehicles', dtype=str)
my_df.to_csv(file_name_csv, index=None, header=True)
lines = my_df.shape[0]
if lines == 1:
    print("{0} line was imported to {1}".format(lines, file_name_csv))
else:
    print("{0} lines were imported to {1}".format(lines, file_name_csv))
