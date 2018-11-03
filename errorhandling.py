''' Handling Error '''
#use keyword raise to customize error
try:
	x=int(input("Number A: "))
	y= int(input("Number B: "))
	
	print(x//y)
except ZeroDivisionError as e:
	print("ERROR",e)
else:
	print(x+y)
finally :
	print(" I cannot divide a number by Zero :(")
