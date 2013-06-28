# Book p 78
# http://lyle.smu.edu/~tylerm/courses/cse3353/code/bst.txt
# http://cslibrary.stanford.edu/110/BinaryTrees.html
# http://python.dzone.com/articles/algorithm-week-binary-search-0
# http://www.sirver.net/blog/2011/07/28/binary-search-trees/


# search
# travelsal
# insertion
# deletion

class Node:
	
	def __init__(self,left=None,right=None,data = None):
		self.left = left
		self.right = right
		self.data = data

	def lookup(self,key):
		if self.data == None:
			return None
		if self.data == key:
			return True
		elif key <= self.data and self.left == None:
			return None
		elif key <= self.data and self.left != None:
			self.left.check(key)
		elif key > self.data and self.right == None:
			return None
		elif key > self.data and self.right != None:
			self.rigt.check(key)

	def insert(self,key):
		if self.data == None:
			self.data == key
		elif key <= self.data and self.left == None:
			self.left = Node(None,None,key)
		elif key <= self.data and self.left != None:
			self.left.insert(key)
		elif key > self.data and self.right == None:
			self.right = Node(None,None,key)
		elif key > self.data and self.right != None:
			self.rigt.insert(key)

	def p(self):
		if self.data == None:
			print "N"
		else:
			print self.data
			if self.left != None:
				self.left.p()
			elif self.right != None:
				self.right.p()


# A Tree class is basically a pointer to its first node
# so is of node class
class Tree:

	def __init__(self):
		# This is just a pointer to the first node! not a node itself!
		# It is like a head pointer in linked list
		self.root = Node(None,None,None)

	def insert(self,key):
		self.root.insert(key)

	def lookup(self,key):
		self.root.lookup(key)

	def p(self):
		self.root.p()

	def pp(self):
		print self.root.data

t = Tree()
t.insert(5)
t.insert(10)
t.insert(2)
t.pp()



