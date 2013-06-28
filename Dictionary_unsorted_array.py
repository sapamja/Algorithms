# Fundamental operations:
# Search
# Insert
# Delete
# Succesor
# Predecessor
# Minimum key
# Maximum key

# Could be implemented with:
# Sorted array
# Unsorted array
# Linked list
# Binary search trees p. 77
# Hash tables p. 89
# Other p. 367

# ------------------------------
# Some links
# http://lyle.smu.edu/~tylerm/courses/cse3353/slides/l8-handout.pdf
# http://www.laurentluce.com/posts/python-dictionary-implementation/
# http://lyle.smu.edu/~tylerm/courses/cse3353/code/dlist.txt

import sys

class Item:
	
	def __init__(self,key=None,value=None):
		self.key = key
		self.value = value

	def __str__(self):
		return str(self.key)+"->"+str(self.value)

# This implementation of dictionary allows for the same keys with different values
class Dictionary:
	
	def __init__(self):
		self.array = []

	def insert(self,key,value):
		# Insert simply new Item with key and value at the end
		# No need to name this new value
		self.array.append(Item(key,value))

	def search(self,key):
		for it in self.array:
			if it.key == key:
				return it
		return None 

	def delete(self,key,value):
		for it in self.array:
			if it.key == key and it.value == value:
				self.array.remove(it)

	def __str__(self):
		outstring = "{ "
		for it in self.array:
			outstring += it.__str__() + " "

		outstring += "}"
		return outstring

# This implementation does not allow for the same keys with different values
# Add function which checks if the key already exists and update insert and delete 
# functions
class Dictionary2:
	
	def __init__(self):
		self.array = []

	def exist(self,key):
		for it in self.array:
			if it.key == key:
				return True	
		return False

	def search(self,key):
		for it in self.array:
			if it.key == key:
				return it
		return None 

	def insert(self,key,value):
		# First we need to check if such key already exists
		if self.exist(key):
			print "Error: Key already exists"
		else:
			self.array.append(Item(key,value))

	def delete(self,key):
		for it in self.array:
			if it.key == key:
				self.array.remove(it)

	def __str__(self):
		outstring = "{ "
		for it in self.array:
			outstring += it.__str__() + " "

		outstring += "}"
		return outstring

	# Return a list of keys
	def keys(self):
		k = []
		for it in self.array:
			k.append(it.key)
		return k

d = Dictionary()
d.insert("a",2)
d.insert("b",4)
d.insert("d","kot")
d.insert("w","wwww")
d.delete("d","kot")
print d.search("b")
print d

dd = Dictionary2()
dd.insert("a",2)
dd.insert("b",4)
dd.insert("d","kot")
dd.insert("w","wwww")
dd.delete("d")
dd.insert("a",10)
print dd.search("b")
print dd








