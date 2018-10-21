def selection(arr):
	for i in range(len(arr)):
		min= i		
		for j in range(i+1,len(arr)):
			if arr[min] > arr[j] :
				min=j
				
				
		arr[min],arr[i]=arr[i],arr[min]
			

 
	return arr






arr=[231,23,12,65,768,32,54,12,86,89,9]

print(selection(arr))