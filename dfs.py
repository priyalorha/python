''' dfs uses stack, visit the nearest node from source,set source to the nearest node'''



lip={}

def addEdge(source,destination):
	if lip.has_key(source) :
		lip[source]=lip[source]+[destination]
	else:
		lip[source]=[destination]
	if lip.has_key(destination):
			lip[destination]=lip[destination]+[source]
	else:
		lip[destination]=[source]

		
		
		
addEdge(0, 1) 
addEdge(0, 2) 
addEdge(1, 2) 
addEdge(2, 0) 
addEdge(2, 3) 
addEdge(3, 3) 	
addEdge(4,4)
visited=[]

def dfs(source):	
	node=lip.keys()	
	q=[]	
	visited=dict.fromkeys(node,False)	
	q.insert(0,source)
	visited[source]=True
	print(source)
	while q:		
	
		
		#print(source)
		for i in lip[source]:			
			if visited[i]  ==False:
				
				q.insert(0,i)
		while q:
			source=q.pop()
			
			if visited[source]==False:
				visited[source]=True
				print(source)
				break
			
		
		

	if(node!=None and len(q)==0):			
		
		for i in visited:
			if visited[i]==False:
				print(i)
				

	
		



for i in lip:
	print("{} {}".format(i,lip[i]))

dfs(4)

