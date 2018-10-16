

''' Array rotation 
#[5,4,8,2] ,2

#[8,2,5,4]'''

def rot(arr,n):

	n%=len(arr)
	h=arr[0:n]
	h1=arr[n:]
	arr=h1+h
		
		
		
		
		
		
		
		
		
		
		
		
	return arr



arr=[12,2,3,45,1]



print(rot(arr,3))

		
		
	