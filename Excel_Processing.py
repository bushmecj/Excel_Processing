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

def usage():
    #TODO: Add usage output here
    pass

def read_file(file_name):
    pass

def main():
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
    '''
    Steps
    1. Add opt step for CLI processing
    2. Check file is an xlsx file
    3. Read into pandas
    4. Process
    5. Write out using xlslx writer

    Final:
    Create .exe of python program

    Future Changes
    Add Flask? Module for GUI interface replacement
    '''
if __name__ == "__main__":
    main()