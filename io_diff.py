# -*- coding: utf-8 -*-

"""
Compare two IOS config files and return the results of lines matched next to each other.

@version: 0.1   -24/02/2020 initial program design, structure, pseudocode
                -24/02/2020 

Takes 2 cli arguments, pointers to files, returns single csv file.
Reads lines from first file and writes to csv file column 1.
Reads line one by one from second file and compares to lines in csv column 1.
If lines match, write line to column 2 of matching row in column 1 in csv file.
If no match found, write line to column 3, keeping track of current row.

Options:
-add optional arguments:
    print matching lines to screen
    print unmatched lines to screen
    print lines in file 1 that are not in file 2
    print lines in file 2 that are not in file 1
    merge 2 files and print to screen or output to csv
    

Pseudocode:
-check arguments given, if not print help
-verify files exist and both can be opened, if not, print error
-create and open new csv file in write mode
-open file 1 specified in arguments
    -read lines from file, ignore lines with special chars such as "!"
    -write lines to column 1 in csv file
-open file 2 specified in arguments
    -read first line and compare to all lines in column 1 of csv
        -if match
            -write line to column 2 in matching row for column 1
        -if no match
            -write line to column 3
            -add one to row number

-save and close csv
-close files 1 and 2
         
-test
"""






































