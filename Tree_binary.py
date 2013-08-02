# Lets define a binary tree

class Node:
	def __init__(self,left,right,value):
		self.left = left
		self.right = right
		self.value = value

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def get_value(self):
		return self.value

# The tree is actually a pointer to a root node
tree_root = Node(None,None,5)