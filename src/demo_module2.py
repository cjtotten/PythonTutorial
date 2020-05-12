'''
Created on May 12, 2020

@author: cjtotten
'''
#import mymodule as mx
from mymodule import person1 as mx
import platform

a = mx["age"]
print(a)

x = dir(platform)
print(x)