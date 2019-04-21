''' bfs uses queue, visit all the nearest node from source, once all the vertex is visited 
change the source to the first visited node'''



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

def bfs(source):	
	node=lip.keys()	
	q=[]	
	visited=dict.fromkeys(node,False)	
	q.append(source)
	visited[source]=True
	while q:		
		source=q.pop(0)
		
		print(source)
		for i in lip[source]:			
			if visited[i]  ==False:
				
				q.append(i)
				visited[i]=True
				'''edge case'''
		if(node!=None and len(q)==0):			
			q=node
			for i in visited:
				if visited[i]==False:
					print(i)
		break			
		
def dfs(source):
	node=lip.keys()	
	q=[]	
	visited=dict.fromkeys(node,False)
	
		



for i in lip:
	print("{} {}".format(i,lip[i]))
bfs(4)

