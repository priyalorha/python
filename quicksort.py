#put all the elements less than pivot on left,and elements greater than pivot on right
def partition(arr,low,high):
	pivot=arr[high]
	
	leftmark=low-1
	
	for j in range(low,high):
		if arr[j]<=pivot:
			leftmark=leftmark+1
			#swap
			arr[leftmark],arr[j]=arr[j],arr[leftmark]

	#swap
	arr[leftmark+1],arr[high]=arr[high],arr[leftmark+1]
	#print("QUICK",arr)
	return leftmark+1



def quick(arr,low,high):
	
	if low <high:
	
		part=partition(arr,low,high)
		#print( arr)
		
		quick(arr,low,part-1)
		quick(arr,part+1,high)
	return arr


arr=[231,23,65,768,32,54,12,86,89,9]

print(quick(arr,0,len(arr)-1))

print(arr)

