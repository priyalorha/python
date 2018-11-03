'''' Lamba functions /anonymous function  '

We use lambda functions when we require a nameless function for a short period of time.

In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
'''
import random
from functools import reduce

#square
square =lambda x:x**2

print(square(8))

# adding two numbers

f = lambda x, y : x + y
 
print(f(10,15))
 
 #finding minimum of two numbers
 
min=lambda x,y : x if x < y else y

print("minimum of 8,9 is {}".format(min(8,9)))




'''' filter 
The filter function applies a predicate to a sequence:


The filter() function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which contains items for which the function evaluats to True.



 ''' 

myList = [random.randint(10,100)  for x in range (7)]
print("my initial list ",myList)
hi=list(filter(lambda num:(num%5==0),myList))

print("number divisible by 15 ",hi)


''' Reducing a List
The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value. 

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
Continue like this until just one element is left and return this element as the result of reduce() '''


lis=[34,232,4324,232,5324,13221,423]

hi = reduce((lambda x,y:x+y),lis)
print ("reduce function",hi)

# calculating a sum of 0-100

print(reduce(lambda x,y:x+y,range(101)))

''' map function  


Map applies a function to all the items in an input_list.'''

hi=list(map((lambda x,y: x+y),lis,myList))

print("Map",hi)


