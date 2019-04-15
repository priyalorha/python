class Node :
	def __init__(self,data):
		self.left=None
		self.right=None
		self.value=data

root=None

def insert(root,data):
	if root == None:
		return Node(data)
	elif root.left==None:
		root.left=Node(data)
		return root.left
	elif root.right==None:
		root.right=Node(data)
		return root.right
	

	
a=insert(root,52)