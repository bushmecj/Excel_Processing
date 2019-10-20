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

CLI_mode = False

def usage():
    #TODO: Add usage output here
    pass

def read_file(file_name):
    pass

def run_using_command_line_interface():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:hu', ['help', 'file='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ('-f', '--file'):
            print('file option select')
            read_file(a)
        if o in ('-h', '--help'):
            usage()
            sys.exit(2)
        print('o: ', o)
        print('a: ', a)
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
    2. Check file is an xlsx file
    3. Read into pandas
    4. Process
    5. Write out using xlslx writer

    Final:
    Create .exe of python program
    pip install auto-py-to-exe

    Future Changes
    Add tkinter Module for GUI interface replacement
    os.path.getmtime --> Last modified 
    '''
if __name__ == "__main__":
    main()