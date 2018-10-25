class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
	
class Tree(Node):

	def __init__(self):
	
		return
	def root(self,value):
		root=Node(value)
		return root
	
	def left(self,root,value):
		if root==None:
			root=Node(value)
		else:
			root.left_child=Node(value)
		return root.left_child
	def right(self,root,value):
		if root==None:
			root=Node(value)
		else:
			root.right_child=Node(value)
		return root.right_child
		

def inorder(root):
		if root==None:
			return
		else:
			inorder(root.left_child)
			print(root.value)
			inorder(root.right_child)	
def postorder(root):
		if root==None:
				return
		else:
			inorder(root.left_child)
			inorder(root.right_child)
			print(root.value)
			
def preorder(root):
		if root==None:
				return
		else:
			print(root.value)
			inorder(root.left_child)
			inorder(root.right_child)
			
				
			
			
Tree=Tree()
root=Tree.root(15)
left=Tree.left(root,8)
right=Tree.right(root,12)
h=Tree.right(left,5)
x=Tree.left(h,4)
p=Tree.right(x,92)

inorder(root)
print(postorder)
postorder(root)
print(preorder)
preorder(root)