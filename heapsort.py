def heapify(arr,n,i):
	largest= i 
	left=2*i +1 
	right=2*i+2
	
	#check left,check right find the largest:
	if left < n and arr[i] < arr[left]:
		largest=left
	if right < n and arr[largest] <arr[right]:
		largest=right
		
		# swap the root with the largest, and heapify for the new heap
	if largest != i:
		arr[i],arr[largest]=arr[largest],arr[i]
		
		heapify(arr,n,largest)
		print (arr)
		
		
		
		
		
def heapsort(arr,low,high):
	n=len(arr)
	#initial heapify
	for i in range(n,-1,-1):
		heapify(arr,n,i)
	# remove the largest , and re run 
	for i in range (n-1,0,-1):
		arr[i],arr[0]=arr[0],arr[i]
		heapify(arr,i,0)


arr=[231,23,65,768,32,54,12,86,89,9]
#arr=[1,5,2]

#arr=[213,12,54,1]
print(arr)
low,high=0,len(arr)
#print(arr,low,high)

print(heapsort(arr,low,high))

print(arr)

