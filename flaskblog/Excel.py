import time
import pandas as pd
import wtforms


# Theme
#Varibles
TodaysDate = time.strftime("%d-%m-%Y")
EXCEL_FILE = 'static/Excel_Data_Entry.xlsx'
#CSV_FIlE = 'Excel_Data_Entry.csv'
df = pd.read_excel(EXCEL_FILE)
#df2 = pd.read_csv(CSV_FIlE)












new_record = pd.DataFrame(values, index=[0])
df = pd.concat([df, new_record], ignore_index=True)
df.to_excel(EXCEL_FILE,sheet_name=TodaysDate, index=False)

print()