'''
Created on May 11, 2020

@author: cjtotten
'''
# function with arbitrary arguments
def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

# default parameter value
def my_function2(country = "USA"):
  print("I am from " + country)

my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")

# passing a list as a function
def my_function3(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function3(fruits)

'''
Recursion is when a function calls itself; you can loop thru data to reach a result.
'''
def tri_recursion(k):
  if(k > 0):
    print('k: ' + str(k))
    result = k + tri_recursion(k - 1)
    print('result is: ', result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
