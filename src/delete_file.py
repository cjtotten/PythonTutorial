'''
Created on May 19, 2020

@author: cjtotten
'''
import os

if os.path.exists("testfile2.txt"):
    os.remove("testfile2.txt")
    print("The file has been deleted!")
else:
    print("The file does not exist")