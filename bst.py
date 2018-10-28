''' BST or a binary search tree, where left < Root < Right (Recurssive)
They allow fast lookup, addition and removal of items, and can be used to implement either dynamic sets of items, or lookup tables that allow finding an item by its key

Algorithm		Average	Worst case
Space		O(n)	O(n)
Search		O(log n)	O(n)
Insert		O(log n)	O(n)
Delete		O(log n)	O(n) '''

import random
class Node :
	def __init__(self,data):
		self.left=None
		self.right=None
		self.value=data
		
		
def insert(root,data):
	if root == None:
		root= Node(data)
		return root
	elif data < root.value :
		if root.left == None:
			root.left=Node(data)
		else :
			insert(root.left,data)
	elif data > root.value:
		if root.right==None:
			root.right=Node(data)
		else:
			insert(root.right,data)
	 

def inorder(root):
	#inorder traversal prints left - root - right
	if root !=None:
		inorder(root.left)
		print(root.value)
		inorder(root.right)
		
def preorder(root):
	# preorder traversal prints root - left -right
	if root !=None:
		print(root.value)
		preorder(root.left)		
		preorder(root.right)
		
def postorder(root):
	# post order traversal prints left-right-root
	if root !=None:
		
		preorder(root.left)		
		preorder(root.right)
		print(root.value)
		
def search(root,data):
		print(root.value)

		if root !=None :
			if root.value==data:
				print(True)
			elif  data  < root.value:
				
				search(root.left,data)
			
			elif data > root.value:
					
					search(root.right,data)
				
		
			
	
		
		
list1=[]
count=0
a=None
a=insert(None,random.randint(0,20))
list1.append(a.value)
for i in range(5):

		k=random.randint(0,20)
		list1.append(k)
		insert(a,k)
h=a
print("inorder" )
print(inorder(h))
h=a
print("postorder" )
print(postorder(h))
h=a
print("preorder")
print(inorder(h))


print(list1)
h=a
search_ele=int(input('Enter the number:'))
print(search(h,search_ele))