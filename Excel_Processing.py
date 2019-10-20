'''
Description: This program will accept an excel file and automatically process it.
Processing will include aggregating floats by name.

Author: Chris Bushmeyer

Created: 10/20/19

Last Modified: 10/20/19
'''

import pandas as pd
import getopt
import xlsxwriter
import os
import sys
from tkinter import *

CLI_mode = True

def usage():
    #TODO: Add usage output here
    pass

def concat_quarter_to_df(df):
    quarter = df['Date'].dt.quarter
    quarter.rename('Quarter')
    df = pd.concat([df,quarter], axis = 1)

    return df

def read_file(file_name):
    '''
    Steps:
    1. Receipts
    2. Expenditures
    3. Contributions Made
    '''
    excel_tabs = ['Receipts', 'Expenditures', 'Contributions Made']
    for tab in excel_tabs:
        if tab != 'Receipts':
            break
        receipts_df = pd.read_excel(file_name, sheet_name=tab, headers = 0)
        receipts_df = concat_quarter_to_df(receipts_df)
        print(receipts_df['Date'].dt.quarter)
        print(receipts_df)

def run_using_command_line_interface():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:o:hu', ['help', 'file=', 'output='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ('-o', '--output'):
            #set output file name and path
            output_name = a
        if o in ('-f', '--file'):
            print('file option select')
            print(o, ' ', a)
            read_file(a)
        if o in ('-h', '--help'):
            usage()
            sys.exit(2)
        #print('o: ', o)
        #print('a: ', a)
    for arg in args:
        print('arg: ', arg)

def run_using_gui():

    window = Tk()
    window.title('Please select a file to process')
    Label(window, text="What file would you like to process:", font="non 12 bold").grid(row=1, column=0, sticky=W)
    textentry = Entry(window, width=20,)
    textentry.grid(row=2, column = 0, sticky=W)
    #button_select = Button(window, 'Select').grid(row=2, column=1)
    window.mainloop()

def main():
    if CLI_mode:
        run_using_command_line_interface()
    else:
        run_using_gui()
    
    '''
    Steps
    1. Add opt step for CLI processing
    2. Output file selection
    3. Check file is an xlsx file
    4. Read into pandas
    5. Process
    6. Write out using xlslx writer

    Final:
    Create .exe of python program
    pip install auto-py-to-exe

    Future Changes
    Add tkinter Module for GUI interface replacement
    os.path.getmtime --> Last modified 
    '''
if __name__ == "__main__":
    main()