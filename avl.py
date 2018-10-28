''' AVL tree (named after inventors Adelson-Velsky and Landis) is a self-balancing binary search tree
 In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property.
 Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where {\displaystyle n} n is the number of nodes in the tree prior to the operation. 
 
 Algorithm		Average	Worst case
Space		{\displaystyle O(n)} O(n)	{\displaystyle O(n)} O(n)
Search		{\displaystyle O(\log n)} O(\log n)[1]	{\displaystyle O(\log n)} O(\log n)[1]
Insert		{\displaystyle O(\log n)} O(\log n)[1]	{\displaystyle O(\log n)} O(\log n)[1]
Delete		{\displaystyle O(\log n)} O(\log n)[1]	{\displaystyle O(\log n)} O(\log n)[1]
 
 
'''


import random
class Node :
	def __init__(self,data):
		self.left=None
		self.right=None
		self.value=data