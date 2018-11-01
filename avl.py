''' AVL tree (named after inventors Adelson-Velsky and Landis) is a self-balancing binary search tree
 In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property.
 Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where {\displaystyle n} n is the number of nodes in the tree prior to the operation. 
 
 AVL trees require the height difference between left,and right tree be +/- 1.
 Worst case is when the right tree has height +1 more than left for every node
 
 Algorithm		Average	Worst case
Space		{\displaystyle O(n)} O(n)	{\displaystyle O(n)} O(n)
Search		{\displaystyle O(\log n)} O(\log n)[1]	{\displaystyle O(\log n)} O(\log n)[1]
Insert		{\displaystyle O(\log n)} O(\log n)[1]	{\displaystyle O(\log n)} O(\log n)[1]
Delete		{\displaystyle O(\log n)} O(\log n)[1]	{\displaystyle O(\log n)} O(\log n)[1]
 
rotation rule explanation: https://medium.com/@randerson112358/avl-trees-a7b4f1fa2d1a
'''


import random
# Python code to insert a node in AVL tree 
  
# Generic tree node class 
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree(object): 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
  
  
# Driver program to test above function 
avlTree = AVL_Tree() 
root = avlTree.insert(None,random.randint(0,200))
for i in range(5):

		k=random.randint(0,200)
		print (k)
		
		root=avlTree.insert(root,k)
		#print (root)
		
		
print("Preorder traversal of the", 
      "constructed AVL tree is") 
avlTree.preOrder(root) 
print() 