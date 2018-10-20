def bubble(arr):
	leng=len(arr)
	
	i=0
	
	for i in range(0,leng):
		#keys=arr[i]
		for j in range(0,leng):
			if(arr[i]<arr[j]):
				arr[i],arr[j]=arr[j],arr[i]
				
				
				
	return arr

	
	
arr=[231,23,12,65,768,32,54,12,86,89,9]

print(bubble(arr))