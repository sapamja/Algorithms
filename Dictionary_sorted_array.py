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
# http://lyle.smu.edu/~tylerm/courses/cse3353/code


# Dictionary with sorted array!!!

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

	def exist(self,key):
		for it in self.array:
			if it.key == key:
				return True	
		return False 
	
	def shift_up(self,n):
		l = len(self.array)
		self.array.append(Item())
		i = l
		while i >= n:
			self.array[i] = self.array[i-1]
			i -= 1

	def shift_down(self,n):
		l = len(self.array)
		for i in range(n,l-1):
			self.array[i] = self.array[i+1]
		del self.array[l-1]

	def find_next(self,key):
		# Finds first key0 > key
		# If doesn't find, returns index outside of the array 
		l = len(self.array)
		i = 0
		while i < l and self.array[i].key < key:
			i += 1
		return i

	# n+n+n+1 = 3n+1 ~ O(n)
	def insert(self,key,value):
		if self.exist(key):
			print "key already exists"
		else:	
			p = self.find_next(key)
			self.shift_up(p)
			self.array[p] = Item(key,value)

	# n+n+n = 3n ~ O(n)
	# Could be improved if exist also returned an index where
	def delete(self,key):
		if self.exist(key):
			n = self.search(key)
			self.shift_down(n)

	# Search could be binary here so log n
	def search(self,key):
		for i in range(len(self.array)):
			if self.array[i].key == key:
				return i
		return None 

	def pred(self,key):
		k = self.search(key)
		return self.array[k-1]

	# The book says here that this should be O(1) but how do we know
	# where given item with k sits?
	def succ(self,key):
		k = self.search(key)
		return self.array[k+1]

	# O(1)
	def max(self):
		return self.array[-1]

	# O(1)
	def min(self):
		return self.array[0]

	def __str__(self):
		outstring = "{ "
		for it in self.array:
			outstring += it.__str__() + " "

		outstring += "}"
		return outstring


d = Dictionary()
d.insert(5,15)
d.insert(7,20)
d.insert(3,20)
d.insert(9,20)
d.insert(1,20)
#print d
#d.delete(5)
#print d
#d.delete(3)
d.insert("ala","kot")
d.insert("ola","pies")
print d
#d.delete("ala")
#print d.max()
#print d.min()
print d.succ(7)
print d.pred(7)





