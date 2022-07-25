import pandas as pd
import glob



#combine all the excel files in the folder that have the same user and date into one excel file
def combine_excel_files(user, date):
    #get all the excel files in the folder that have the same user and date
    files = glob.glob('/Users/jessicahung/Desktop/flaskblog/static/excel_files/' + user + '_' + date + '*.xlsx')
    #combine all the excel files in the folder that have the same user and date into one excel file
    combined_excel_file = pd.concat([pd.read_excel(f) for f in files])
    #save the combined excel file
    combined_excel_file.to_excel('/Users/jessicahung/Desktop/flaskblog/static/excel_files/' + user + '_' + date + '_combined.xlsx', index=False)
    #return the combined excel file
    return combined_excel_file
