graph={'a':{'b':8,'c':2},
	'b':{'a':8,'f':13},
	'c':{'a':2,'d':2},
	'd':{'a':5,'b':2,'c':2,'e':1,'f':6,'g':3},
	'e':{'c':5,'d':1,'g':1},
	'f':{'b':13,'d':6,'g':2,'h':3},
	'g':{'e':1,'d':3,'f':2,'h':6},
	'h':{'g':6,'f':3}}
	
	
def dijkstra(graph,start,destination):
	shortest_distance={}
	predecessor={}
	unseenNodes=graph
	infinity=999999
	path=[]
	shortest_distance={key:infinity for key in graph}
	shortest_distance[start]=0
	
	while unseenNodes:
		minNode=None
		
		for node in unseenNodes:
			

			if minNode is None:
				minNode=node
			elif shortest_distance[node]<shortest_distance[minNode]:
				minNode=node
		print(graph[minNode].items())
		for childNode,weight in graph[minNode].items():
			if weight + shortest_distance[minNode]<shortest_distance[childNode]:
				shortest_distance[childNode]=weight + shortest_distance[minNode]
				predecessor[childNode]=minNode
		unseenNodes.pop(minNode)
		
	currentNode=destination
	
	while currentNode!=start:
		try:
			path.insert(0,currentNode)
			currentNode=predecessor[currentNode]
		except KeyError:
			print('Path not reachable')
			break
	if shortest_distance[destination]!=infinity:
		print('Shortest distance ' + str(shortest_distance[destination]))
		print('and the path is ' + str(path))
		
	
	
dijkstra(graph,'a','h')
