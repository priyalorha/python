''' List Comprehension 

Syntax [ expression for item in list if conditional ]'''
import random
list1=[ random.randint(0,200) for x in range (0,10) ]
print (list1)

def hi():
	return random.randint(0,10)**2
# calling function	
list2=[hi() for x in range(0,10)]
print (list2)


#storing even numbers

list3=[x for x in range(100) if x%2==0]
print (list3)

#arrguments
print("list4")
list4=[x+y for x in [3,2,84,1] for y in [1,2,3,4] ]
print(list4)


#Iterating through a string Using List Comprehension

list5=[p for p in('Happiness')]
print(list5)


#transpose

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)