def merge(arr,low,mid,high):
	
	
	left = arr[low:mid+1]
	right=arr[mid+1:high+1]
	
	left_index,right_index,arr_index=0,0,low
	while left_index < len(left) and right_index < len(right) :
		if left[left_index] <= right[right_index]:
			arr[arr_index]=left[left_index]
			left_index+=1
		else:
			arr[arr_index]=right[right_index]
			right_index+=1
			
		arr_index+=1
		
	while left_index < len(left) :
		arr[arr_index]=left[left_index]
		left_index+=1
		arr_index+=1
		
	while right_index < len(right) :
		arr[arr_index]=right[right_index]
		right_index+=1
		arr_index+=1
		
		
		
		
		
		
		
def mergesort(arr,low,high):
	#print(arr)
	if low < high :
		mid= (low +high)//2 
		#print (arr,low,mid,high)
		mergesort(arr,low,mid)
		
		mergesort(arr,mid+1,high)
		
		#print(arr,low,mid,high)
	
		merge(arr,low,mid,high)
		#print(arr)
	return arr
	


arr=[231,23,65,768,32,54,12,86,89,9]
#arr=[1,5,2]

#arr=[213,12,54,1]
print(arr)
low,high=0,len(arr)
#print(arr,low,high)
print(mergesort(arr,low,high))