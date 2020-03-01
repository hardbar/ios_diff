# -*- coding: utf-8 -*-

"""
A simple script to compare two text files and generate an HTML file with the differences.
"""

import difflib

first_file = "ecc1.txt"
second_file = "ecc2.txt"
first_file_lines = open(first_file).readlines()
second_file_lines = open(second_file).readlines()

diff = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)
diff_report = open("diff_report.html", "w")
diff_report.write(diff)
diff_report.close

#def compare(File1,File2):
#    with open(File1,'r') as f:
#        d=set(f.readlines())
#
#
#    with open(File2,'r') as f:
#        e=set(f.readlines())
#
#    open('file3.txt','w').close() #Create the file
#
##    with open('file3.txt','a') as f:
##        for line in list(d-e):
##           f.write(line)
#           
#    for line in list(d-e):
#        print(line)
#    
#    
#file1 = "ecc1.txt"
#file2 = "ecc2.txt"
#compare(file1, file2)








