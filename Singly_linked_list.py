# Info:
# http://alextrle.blogspot.com/2011/05/write-linked-list-in-python.html
# http://kkthegeek.wordpress.com/2010/05/06/linked-list-implementation-in-python/
# http://en.literateprograms.org/Singly_linked_list_(Python)
# http://lyle.smu.edu/~tylerm/courses/cse3353/slides/l7-handout.pdf
# Questions for singly linked lists
# - How reverse singly linked list using recursion and iteration
# - How to find middle element in single linked list with one pass
# - What is the difference between singly and doubly linked list


class Node:

	def __init__(self,next=None,data=None):
		self.next = next
		self.data = data

	def get_next(self):
		# points to the next object of Node class or None
		return self.next

	def get_data(self):
		# poins to data container
		return self.data

	def set_next(self,new_node):
		# sets the value of the next as new node
		self.next = new_node

	def set_data(self,data):
		self.data = data



class LinkedList:
	
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0



	def __str__(self):
		outstr = ""
		n = self.head
		while n:
			outstr = outstr + str(n.get_data()) + " "
			n = n.get_next()
		return outstr

	def isEmpty(self):
		return self.head == None

	def insert_end(self,data):
		# create new node for the data
		new_node = Node(None,data)

		# If list is empty
		# Create first node
		if self.length == 0:
			self.head = new_node
			self.tail = new_node
			self.length += 1
		else:
			self.tail.set_next(new_node)
			self.tail = new_node
			self.length += 1

	def insert_beginning(self,data):
		new_node = Node(None,data)
		if self.length == 0:
			self.head = new_node
			self.tail = new_node
			self.length += 1
		else:
			new_node.set_next(self.head)
			self.head = new_node
			self.length += 1


	# Insert new_node after old_node
	def insert(self,old_node,data):
		# remember to update length
		# remember to update tail
		# there is no empty list case here because we need to give
		# at least one node
		new_node = Node(old_node.get_next(),data)
		old_node.set_next(new_node)
		if self.tail == old_node:
			self.tail = new_node
		self.length += 1

	
	def get_length(self):
		return self.length


	def search(self,x):
		# return pointer to first node with the searched value
		if self.isEmpty():
			return None
		else:	
			item = self.head
			i = 0
			while item != None:
				if item.get_data() == x:
					return i
				item = item.get_next()
				i += 1
			return None	

	def remove_after(self,node):
		# remember to update tail if removed tail
		# remember to update count!
		if node.get_next() != None:
			nextnode = node.get_next()
			node.set_next(nextnode.get_next())
			self.length -= 1
			if nextnode == self.tail:
				self.tail = node

	def get_previous(self,node):
		if node == self.head:
			return None
		else:
			n = self.head
			while n:
				if n.get_next() == node:
					return n
					break
				else:
					n = n.get_next()

	def remove_before(self,node):
		if node != self.head:
			self.length -= 1
			prev_node = self.get_previous(node)
			if prev_node == self.head:
				self.head = node
			else:
				prev_prev_node = self.get_previous(prev_node)
				prev_prev_node.set_next(node)

	# Find m-th element from the end of list
	# Do not use the internal slength counter!
	def find_m_from_end(self,m):
		if m < 0:
			print "m should be larger or equal than 0"
			return None
		if self.isEmpty():
			print "List is empty"
			return None
		else:
			p1 = self.head
			p2 = self.head
			i = 0
			while p1 != self.tail:
				p1 = p1.get_next()
				i += 1
				if i > m:
					p2 = p2.get_next()
			if i <= m:
				print "Element", m,"from end does not exist "
				return None
			else:
				return p2.get_data()



# Add iterator over the list!
a = LinkedList()
a.insert_beginning(0)
a.insert_beginning(10)
a.insert_beginning(20)
a.insert_beginning(30)
a.insert_beginning(40)
a.insert_beginning(50)
a.insert_beginning(60)
a.insert_beginning(70)
a.insert_beginning(80)
a.insert_beginning(90)
print a.find_m_from_end(10)












