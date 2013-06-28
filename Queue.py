''' Queue implementation
FILO - first in  first out
Add elements on the head and remove from tail
The pointers directions from head to tail (next) 
Define class of list element - Item (value, next)
Methods:
- get_next()
- get_value()
- set_next()

Define class of queus - head, tail
Methods:
- enq(value) - add new item at head
- deq() - remove item at tail
		- traverse to the item before tail
		- assign tail to this item
		- remember to set item's next to None
- __init__()
- __str__()

Error handling:
- remove from empty Queue
'''


class Item:
	def __init__(self,value):
		self.value = value
		self.next = None

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next

	def set_next(self,next):
		self.next = next

# None size restricted queue
class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def isEmpty(self):
		return self.head == None

	def __str__(self):
		if self.isEmpty():
			return "The queue is empty"
		else:
			out = ""
			item = self.head
			while item != None:
				out += str(item.get_value())+" "
				item = item.get_next()
			return out

	def enq(self,value):
		new_item = Item(value)
		# if queue empty
		if self.isEmpty():
			self.head = new_item
			self.tail = self.head
		else:
			new_item.set_next(self.head)
			self.head = new_item


	def deq(self):
		# if empty
		if self.isEmpty():
			print "Queue is empty, nothing to dequeue"
		# if only one element
		elif self.head != None and self.head == self.tail:
			item = self.head
			self.head = None
			self.tail = None
			return item.get_value()
		# if more elements
		else:
			item = self.head
			while item.get_next() != self.tail:
				item = item.get_next()
			keep_item = self.tail
			self.tail = item
			item.set_next(None)
			return keep_item.get_value()

# this is a queue with limited space
class lQueue:
	def __init__(self,limit):
		self.head = None
		self.tail = None
		self.limit = limit
		self.size = 0

	def isEmpty(self):
		return self.head == None

	def __str__(self):
		if self.isEmpty():
			return "Queue is empty, nothing to print"
		else:
			out = ""
			item = self.head
			while item != None:
				out += str(item.get_value())+" "
				item = item.get_next()
			return out

	def enq(self,value):
		new_item = Item(value)
		if self.size == self.limit:
			print "Queue full, not possible to add"
			return None
		elif self.isEmpty():
			self.head = new_item
			self.tail = new_item
			self.size += 1
		else:
			new_item.set_next(self.head)
			self.head = new_item
			self.size += 1

	def deq(self):
		if self.isEmpty():
			print "Queue is empty, nothing to remove"
			return None
		elif self.head != None and self.head == self.tail:
			item = self.head
			self.head = None
			self.tail = None
			self.size -= 1
			return item.get_value()
		else:
			item = self.head
			while item.get_next() != self.tail:
				item = item.get_next()
			keep_item = self.tail
			self.tail = item
			item.set_next(None)
			self.size -= 1
			return keep_item.get_value()



# ---- tests ----
b = Queue()
b.enq(1)
b.enq(4)
b.enq(5)
print b


a = lQueue(4)
a.enq(1)
print a," size= ",a.size
a.enq(2)
print a," size= ",a.size
a.enq(4)
print a," size= ",a.size
a.enq(6)
print a," size= ",a.size
a.enq(9)
print a," size= ",a.size
c = a.deq()
print a," size= ",a.size
print c
c = a.deq()
print a," size= ",a.size
print c










