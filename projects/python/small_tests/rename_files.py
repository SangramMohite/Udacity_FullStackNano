import os
import re

def rename_files():
    # list all files in the directory
    file_path = r"C:\Users\Sangram\Documents\workspace\udacity\FullStack\python\prank"
    file_list = os.listdir(file_path)
    os.chdir(file_path)
    for filename in file_list:
        print(" old name: " + filename)
        os.rename(filename, re.sub("\d+","", filename))        
        
    #print(os.listdir(file_path))
    
    # rename file if there is a number in them

rename_files()
