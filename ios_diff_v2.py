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

# ***All imports under here***
import argparse
import sys
import pandas as pd
import numpy as np

# ***Global variables***


# **ALL FUNCTIONS UNDER HERE**

def isValidFile(file1, file2):
    """ Confirms specified files are valid
        Returns an error if it is not found

        Keyword arguments:
        file1 -- first file entered by the user
        file2 -- second file entered by the user
    """   
    try:
        if file1:
            print("{} valid".format(file1))
        if file2:
            print("{} valid".format(file2))
            file2 = file2.read()
    except (FileNotFoundError, NameError):
        print("No such file or directory: {} {}".format(file1, file2))
        sys.exit()



# **MAIN** 
def main():
    """
    This is the main function for the ios_diff.py program
    This module represents the (otherwise anonymous) scope in which the interpreter’s main 
    program executes — commands read either from standard input, from a script file, or from an interactive prompt.
    """
    # argument parser
#    parser = argparse.ArgumentParser(description="Description: Compare two Cisco IOS files.")
#    parser.add_argument("-file1", help="enter full path and filename of first file, ie /var/log/file.log")
#    parser.add_argument("-file2", help="enter full path and filename of second file, ie /var/log/file.log")
#    parser.add_argument("-m", "--menu", help="use text menu prompts for input instead of specifying arguments", action="store_true")
#    args = parser.parse_args()
#    file1 = args.file1
#    file2 = args.file2
    
    # if menu is selected present text menu options
#    if args.menu:
#        file1 = input("Enter filename for file 1: ")
#        file2 = input("Enter a filename for file 2: ")
        
    # check user inputed valid files
    #isValidFile(file1, file2)
    
    # create and join the data frames for the two input files
    with open("ecc1.txt", "r", newline="") as file1, open("ecc2.txt", "r",newline="") as file2, open("ecc1.csv", "w+") as csv_file:
        file1 = [line.strip() for line in file1 if line[0] != "!"]
        file2 = [line.strip() for line in file2 if line[0] != "!"]
        df1 = pd.DataFrame({'A': file1})
        df2 = pd.DataFrame({'B': file2})
        df3 = df1.join(df2)
        df3["Index"] = range(0, len(df3))
        df3.set_index("Index", inplace=True)
        #print(df3.head())
        
        new_data = pd.Series([])
        count = 0
        j = 0
        while count < len(df3):
            for i in range(len(df3)):
                if df3["A"][i] == df3["B"][j]:
                    new_data[i] = df3["A"][i]
            j += 1
            count += 1
    
        df3.insert(2, "Matches", new_data)
        pd.set_option("display.max_rows", 1000)
        df3.to_csv(csv_file, line_terminator="")
    
    # df3["Result"] = np.where(df3["A"] == df3["B"], "Match", "No match")  # creates a third column with result of comparison
    new_list = []
    for k in range(len(df3)):
        if str(df3["Matches"][k]) != "nan":
            #print(str(df3["Matches"][k]))
            new_list.append(df3["Matches"][k])

       # Need to parse new_list and write to new column in data frame !!!! can't this be done without creating a new list ????

if __name__ == "__main__":
    main()
    