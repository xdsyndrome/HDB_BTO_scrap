import schedule, time
from extractData import extractData
import pandas as pd
from openpyxl import load_workbook
from writeExcel import writeExcel

def main():

    # Define variables
    timeList = ["00:52:00", "00:52:10"]
    excelfile2 = r"C:\Users\xiaod\Desktop\Misc Projects\1. HDB SBF Scrape\SBF2room.xlsx"
    excelfile3 = r"C:\Users\xiaod\Desktop\Misc Projects\1. HDB SBF Scrape\SBF3roomOrLarger.xlsx"

    # Run function to extract data based on schedule

    df2 = pd.DataFrame(columns = ["Row", "No of units", "Number of Applicants", "Elderly", "FT", "ST", "Singles", "Overall", "Time"])
    df3 = pd.DataFrame(columns = ["Row", "No of units", "Number of Applicants", "FT", "ST", "Overall", "Time"])

    def finalOutput(df2, df3, excelfile2, excelfile3):
        # Initiate overall dataset

        outputPerRun2, outputPerRun3 = extractData()

        results2 = pd.Series(outputPerRun2[0], index = df2.columns)
        results3 = pd.Series(outputPerRun3[0], index = df3.columns)

        df2 = df2.append(results2, ignore_index = True)
        df3 = df3.append(results3, ignore_index = True)

        # Open existing excel and append new data into file, returns excelfile
        f2 = writeExcel(excelfile2, df2)
        f3 = writeExcel(excelfile3, df3)
 
    for i in timeList:
        schedule.every().day.at(i).do(finalOutput,df2,df3,excelfile2,excelfile3)
        
    while 1: 
        schedule.run_pending()
        time.sleep(1)

    
if __name__ == "__main__":
    main()