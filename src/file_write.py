'''
Created on May 19, 2020

@author: cjtotten
'''
# overwrite the content
f = open("testfile2.txt", "w")
f.write("Woops! I have deleted content!")
f.close()
# open and read the file after deleting content
f  = open("testfile2.txt", "rt")
print(f.read())#

# create a new file if it does not exist
#f = open("myfile.txt", "x")
f = open("myfile.txt", "w")