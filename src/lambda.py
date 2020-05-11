'''
Created on May 11, 2020

@author: cjtotten
'''

'''
A lamba function is a small anymymous function
lambda arguments : expression
'''
x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))

# use lambda as an anonymous function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(11)

print(mydoubler(3))
