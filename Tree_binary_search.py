import networkx as nx
import matplotlib.pyplot as plt


# Lets play with binary search tree
# - Define node
# - Define tree
# - def: get left, right, value
# - def: set left, right, value
# - Tree traversal
# - Tree insert nodes / build tree
# - Tree search

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

	def set_value(self,value):
		self.value = value

	def set_left(self,value):
		if value == None:
			self.left = None
		else:
			self.left = Node(None,None,value)

	def set_right(self,value):
		if value == None:
			self.right = None
		else:
			self.right = Node(None,None,value)

class Tree:
	def __init__(self):
		self.root = None

	def insert_node(self,node,value):
		# 1. Check if root is None if yes, assign value to root 
		# 2. If not, compare value with node value
		# 3. If lower then check if left child exists
		# 4. If not create it and give it new value
		# 5. If it exists, do recursion on left child
		# 6. Same for right child
		if self.root == None:
			self.root = Node(None,None,value)
		else:
			if value <= node.get_value():
				if node.get_left() == None:
					node.set_left(value)
				else:
					self.insert_node(node.get_left(),value)
			else:
				if node.get_right() == None:
					node.set_right(value)
				else:
					self.insert_node(node.get_right(),value)

	def search(self,value):
		# 1. Check if tree is empty
		# 2. While the node is not None
		# 3. if you find value, return it
		# 4. if you don't, traverse to left or right
		# 5. if you don't find it in tree, say it
		node = self.root
		while node != None:
			if node.get_value() == value:
				return node
			else:
				if value < node.get_value():
					node = node.get_left()
				else:
					node = node.get_right()
		print "Value not found"
		return None			 

	def recursive_search(self,node,value):
		# 1. Check if root is None
		# 2. If not check if root value equals value
		# 3. If yes, return it
		# 4. If not, traverse right or left and return what you find
		if node == None:
			return None
		else:
			if node.get_value() == value:
				#print "here",node.get_value()
				return node
			else:
				if value < node.get_value():
					return self.recursive_search(node.get_left(),value)
				else:
					return self.recursive_search(node.get_right(),value)

	def find_max(self,node):
		node = self.root
		while node.get_right() != None:
			node = node.get_right()
		return node.get_value()

	def find_min(self,node):
		node = self.root
		while node.get_left() != None:
			node = node.get_left()
		return node.get_value()


	def find_parent_node(self,root,node):
		# 1. Check if node is None
		# 2. Check if node is root
		# 3. check if any of the children of the root are equal to node
		# 4. If none of the above, then depending on the value of the node
		# 	recurse left or right
		# 5. Before recursing, remember to check if left or right child exist
		# 	if it does not, it means that the node is not from this tree!
		# 	Check your tree
		if node == None:
			print "Node is None"
		elif node == self.root:
			print "This is a root which has no parent"
		else:
			parent = root
			if (parent.get_left()!= None and parent.get_left() == node):
				return [parent,"left"]
			elif (parent.get_right()!= None and parent.get_right() == node):
				return [parent,"right"]
			else:
				if node.get_value() < parent.get_value():
					if parent.get_left() == None:
						print "Can't find parent in this tree"
					else:
						return self.find_parent_node(parent.get_left(),node)
				else:
					if parent.get_right() == None:
						print "Can't find parent in this tree"
					else:
						return self.find_parent_node(parent.get_right(),node)


	def find_max_left(self,node):
		# Largest value in left subtree below node
		if node.get_left() == None:
			return node
		else:
			node = node.get_left()
			while node.get_right() != None:
				node = node.get_right()
			return node


	def find_min_right(self,node):
		# Largest value in left subtree below node
		if node.get_right() == None:
			print "No right node"
			return node
		else:
			node = node.get_right()
			while node.get_left() != None:
				node = node.get_left()
			return node

	def isLeaf(self,node):
		if node.get_left() == None and node.get_right() == None:
			return True
		else:
			return False

	def remove_leaf(self,node):
		if self.root == None:
			print "Tree is empty"
		if self.isLeaf(node):
			if node == self.root:
				self.root = None
			else:
				parent = self.find_parent_node(self.root,node)
				parent_node = parent[0]
				child = parent[1]
				if child == "left":
					parent_node.set_left(None)
				else:
					parent_node.set_right(None)
		else:
			print "Error in remove leaf: Not a leaf"


	def remove_node(self,node):
		# For some info on removing the node see here:
		# http://webdocs.cs.ualberta.ca/~holte/T26/del-from-bst.html
		# I need 5 functions for the remove node to work
		# - isLeaf
		# - find_max_left
		# - find_min_right
		# - find_parent_node
		# - remove_leaf
		# When writing your finctions be careful with:
		# - always check if tree is not empty
		# - always check if your node to remove is root
		# - check if the node to remove is not None!
		# - check if leaf is root
		# - check if left or right exists
		# - be careful when renaming nodes
		# - Also note that function find_parent_node returns a list of two elements!
		
		if self.root == None:
			print "Tree is empty"
		elif node == None:
			print "Nothing to remove"
		elif self.isLeaf(node):
			if node == self.root:
				self.root = None
			else:
				self.remove_leaf(node)
		else:
			if node.get_left() != None:
				maxnode = self.find_max_left(node)
				if self.isLeaf(maxnode):
					new_value = maxnode.get_value()
					self.remove_leaf(maxnode)
					node.set_value(new_value)
				else:
					node.set_value(maxnode.get_value())
					self.remove_node(maxnode)
			else:
				maxnode = self.find_min_right(node)
				if self.isLeaf(maxnode):
					new_value = maxnode.get_value()
					self.remove_leaf(maxnode)
					node.set_value(new_value)
				else:
					node.set_value(maxnode.get_value())
					self.remove_node(maxnode)
		

# ---------------------------------------
# Non class functions

def traversal_preorder(node):
	# 1. Check if tree is empty
	# 2. If empty, give a message
	# 3. If not empty, print value of the current node
	# 4. If left child exists recurse/traverse to left
	# 5. If right child exists recurse/traverse to right
	if node == None:
		print "Tree is empty"
	else:
		print node.get_value()
		if (node.get_left() != None):
			traversal_preorder(node.get_left())
		if (node.get_right() != None):
			traversal_preorder(node.get_right())

# This travelsal returns a sorted list of nodes
def traversal_inorder(node):
	if node == None:
		print "Tree is empty"
	else:
		if (node.get_left() != None):
			traversal_inorder(node.get_left())
		
		print node.get_value()
	
		if (node.get_right() != None):
			traversal_inorder(node.get_right())


def traversal_postorder(node):
	if node == None:
		print "Tree is empty"
	else:
		if (node.get_left() != None):
			traversal_postorder(node.get_left())
		if (node.get_right() != None):
			traversal_postorder(node.get_right())
		print node.get_value()

# --------------------------
# Functions for testing tree codes!

def get_nodes(root,G):
	if root != None:
		G.add_node(root.get_value())

		if (root.get_right() != None):
			get_nodes(root.get_right(),G)
			G.add_edge(root.get_value(),root.get_right().get_value())

		if (root.get_left() != None):
			get_nodes(root.get_left(),G)
			G.add_edge(root.get_value(),root.get_left().get_value())


def plot_tree(root):
	# http://stackoverflow.com/questions/11479624/is-there-a-way-to-guarantee-hierarchical-output-from-networkx
	G = nx.DiGraph()
	get_nodes(root,G)
	if len(G.nodes())==0:
		print "Tree is empty"
	else:
		pos=nx.graphviz_layout(G,prog='dot')
		nx.draw(G,pos,with_labels=True,arrows=False,node_size=1000)
		plt.show()


def build_tree(mylist):
	if len(mylist) == 0:
		print "List is empty"
		return None
	else:
		t = Tree()
		for l in mylist:
			t.insert_node(t.root,l)
		return [t,mylist]

def thisnode(tree,value):
	return tree.recursive_search(tree.root,value)

def test_tree(tree):
	nodes = tree[1]
	for n in nodes:
		print "remove",n
		t = build_tree(nodes)
		t[0].remove_node(thisnode(t[0],n))


# Node removal testing
t1 = build_tree([5])
t2 = build_tree([5,1])
t3 = build_tree([5,20])
t4 = build_tree([5,1,20])
t5 = build_tree([5,4,3,2])
t6 = build_tree([5,10,15,20])
t7 = build_tree([5,3,20,1,4,10,25])
t8 = build_tree([10,5,8,7,9])

test_tree(t1)
test_tree(t2)
test_tree(t3)
test_tree(t4)
test_tree(t5)
test_tree(t6)
test_tree(t7)
test_tree(t8)

traversal_inorder(t7[0].root)




