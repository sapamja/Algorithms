# Dome info about operations in heap
# http://en.wikipedia.org/wiki/Binary_heap

import random
import networkx as nx
import matplotlib.pyplot as plt


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
		# If value equals None, remove left node
		if value == None:
			self.left = None
		else:
			self.left = Node(None,None,value)

	def set_right(self,value):
		# If value equals None, remove right node
		if value == None:
			self.right = None
		else:
			self.right = Node(None,None,value)

	def isLeaf(self):
		if self.left == None and self.right == None:
			return True
		else:
			return False

class Heap:
	def __init__(self):
		self.root = None


	def attach_at_bottom(self,node,value):
		# this will give me random position at the end of the heap
		
		if self.root == None:
			self.root = Node(None,None,value)
		elif node.isLeaf():
			node.set_left(value)
		elif node.get_left() == None:
			node.set_left(value)
		elif node.get_right() == None:
			node.set_right(value)
		else:
			new_node = random.sample([node.get_left(),node.get_right()],1)[0]
			self.attach_at_bottom(new_node,value)
		
	def swap(self,node):
		if self.root == None:
			print "Heap is empty"
			return None
		elif self.root.isLeaf():
			print "Heap has only root"
			return None
		
		# Go down
		if node.get_left() != None:
			if not node.get_left().isLeaf():
				print "go left"
				self.swap(node.get_left())
			
			if node.get_value() < node.get_left().get_value():
				print "swap left"
				tmp = node.get_value()
				node.set_value(node.get_left().get_value())
				node.get_left().set_value(tmp)

		# Go down
		if node.get_right() != None:
			if not node.get_right().isLeaf():
				print "go right"
				self.swap(node.get_right())
			
			if node.get_value() < node.get_right().get_value():
				print "swap right"
				tmp = node.get_value()
				node.set_value(node.get_right().get_value())
				node.get_right().set_value(tmp)

	



# Non class functions
# Testing functions
def build_heap(mylist):
	if len(mylist) == 0:
		print "List is empty"
		return None
	else:
		h = Heap()
		for l in mylist:
			h.attach_at_bottom(h.root,l)
			h.swap(h.root)
		return h

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

h = build_heap([5,3,20,1,4,10,25,12,11,2,7,22,21,8,9,13])
plot_tree(h.root)

#h = build_heap([5,3,20,30])
#h.swap(h.root)
#plot_tree(h.root)


