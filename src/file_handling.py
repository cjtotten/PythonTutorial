'''
Created on May 19, 2020

@author: cjtotten
'''
f = open("testfile.txt", "rt")
# read the entire file
# read the first five lines
# print(f.read())
# print(f.read(5))
# read the first line
# print(f.readline())
# loop thru file line by line
'''
for x in f:
    print(x)
'''
# cloose a file
#print(f.readline())
#f.close

# append to a file
f = open("testfile.txt", "a")
f.write("Now the file has more content!")
f.close()
# open and read the file after appending
f = open("testfile.txt", "r")
print(f.read())



