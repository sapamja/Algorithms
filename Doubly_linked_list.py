# This is a doubli linked list
# I will use it to test my algorithm for flattening of the list
# with children
# I will use my queue implementation here.

from Queue import *


class Item:
 	def __init__(self,value,next=None,prev=None,child=None):
 		self.value = value
 		self.child = child
 		self.next = next
 		self.prev = prev

 	def set_next(self,next):
 		self.next = next

 	def set_prev(self,prev):
 		self.prev = prev

 	def set_value(self,value):
 		self.value = value

 	def set_child(self,child):
 		self.child = child

 	def get_next(self):
 		return self.next

 	def get_prev(self):
 		return self.prev

 	def get_value(self):
 		return self.value

 	def get_child(self):
 		return self.child

 	def __str__(self):
 		return str(self.get_value())

class dList:
	def __init__(self):
		self.head = None
		self.tail = None


	def isEmpty(self):
		return self.head == None

	# Add at the end, at tail
	def add_item(self,value):
		new_item = Item(value)
		if self.isEmpty():
			self.head = new_item
			self.tail = new_item
		else:
			new_item.set_prev(self.tail)
			self.tail.set_next(new_item)
			self.tail = new_item


	def __str__(self):
		if self.isEmpty():
			return "List is empty"
		else:
			out = ""
			item = self.head
			while item != None:
				out += str(item.get_value())+" "
				item = item.get_next()
			return out 

	def flatten_list(self):
		if self.isEmpty():
			return "List is empty"
		else:
			out = ""
			q = Queue()
			item = self.head
			while item != None or not q.isEmpty():
				print item
				out += str(item.get_value()) + " "
				if item.get_child() != None:
					q.enq(item.get_child())

				if item.get_next() == None:
					if not q.isEmpty():
						item = q.deq()
					else:
						item = None
				else:
					item = item.get_next()
		return out




if __name__ == "__main__":

	a = [0 for i in range(17)]
	a[0] = [5,1,None,5]
	a[1] = [33,2,0,None]
	a[2] = [17,3,1,None]
	a[3] = [2,4,2,8]
	a[4] = [1,None,3,None]

	a[5] = [6,6,None,None]
	a[6] = [25,7,5,10]
	a[7] = [6,None,6,11]
	a[8] = [2,9,None,12]
	a[9] = [7,None,8,None]

	a[10] = [8,None,None,None]
	a[11] = [9,None,None,14]
	a[12] = [12,13,None,15]
	a[13] = [5,None,12,None]

	a[14] = [7,None,None,None]
	a[15] = [21,16,None,None]
	a[16] = [3,None,15,None]

	b = [Item(0,None,None,None) for i in range(17)]
	for i in range(17):
		b[i].set_value(a[i][0])

		next = a[i][1]
		if next:
			b[i].set_next(b[next])
			
		prev = a[i][2]
		if prev: 	
			b[i].set_prev(b[prev])
		
		child = a[i][3]
		if child:
			b[i].set_child(b[child])

	c = dList()
	c.head = b[0]
	c.tail = b[4]

	print c.flatten_list()









