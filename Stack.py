# This is a linked list implementation of a stack p. 38
# With operations:
# push, pop
# Other implementations - dynamic array. Read about advantages in p, 38

''' The plan
1. The class of a stack element
- pointer to next list element
- value field
- Methods:
	* set_next(next)
	* get_next()
	* get_value()
2. The class of a stack
- head pointer - top of the stack
- Methods:
	* __init__() - head = None
	* push(new_data) - adds a new element at the head of the stack
					 - new element points at what head is pointing
					 - update the top
	* pop() - removes the top element of the stack and returns it
			- takes the value of current top to return
			- updates the top pointer
			- returns the value
	* __str__()
	* delete() - assign None to the top
	* isEmpty() - checks if stack empty
4. Error handling - possible problems
	* Tries to pop when stack empty -> return NULL
	* 
'''

# The implementation
class Item:
	def __init__(self,value):
		self.value = value
		self.next = None

	def set_next(self,next):
		self.next = next

	def get_next(self):
		return self.next

	def get_value(self):
		return self.value

class Stack:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		# Check if stack is empty
		return self.head == None

	def __str__(self):
		# If stack is empty, nothing to print
		if self.isEmpty():
			return "Stack is empty"
		else:
			# Not empty, print one by one untill the end
			# Follow next pointers
			out = ""
			i = self.head
			while i != None:
				out += str(i.get_value())+" "
				i = i.get_next()
			return out 	

	def push(self,value):
		# Add new element at the head of stack
		new_item = Item(value)
		# If stack is not empty, ned to assign first next value to 
		# new item
		if not self.isEmpty():
			new_item.set_next(self.head)
		# Then set the head to new item
		self.head = new_item

	def pop(self):
		# remove first item at the head
		# If empty, nothing to remove
		if self.isEmpty():
			return None
		# If not empty, need to keep pointer to current head
		# Then assign head to second element
		# return the value from old head	
		else:
			tmp_head = self.head
			self.head = self.head.get_next()
			return tmp_head.get_value()

# --------------
# Tests

a = Stack()
#print a.isEmpty
a.push(1)
a.push(5)
a.push(10)
a.push(20)
print a
a.pop()
a.pop()
a.pop()
a.pop()
print a
#print a.head.get_value()

























