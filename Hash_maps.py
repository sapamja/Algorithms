# Explain how hash tables work internally. How is hash code
# generated and what will happen to hash code when 2 values are same.
# http://en.wikipedia.org/wiki/Hash_table
# * Hash tables map keys to values
# * Keys are stored in array of buckets or slots
# * Hash tables use function to map a key to an index of array
# * In good hash table, average lookup time does not depend on number of elements
# * In ideal situation each key should be assigned unique bucket
# 	But this is rarely achieved in reality
# 	So collisions happen when two keys fall in the same bucket
# * The idea of hashing is to distribute the entries (key/value pairs) across an array of buckets.
# 	Given a key, the algorithm computes an index that suggests where the entry can be found.

# https://sites.google.com/site/usfcomputerscience/hash-tables-imp
# Python implementation of dictionaries
# See: http://www.laurentluce.com/posts/python-dictionary-implementation/
# http://www.shutupandship.com/2012/02/how-hash-collisions-are-resolved-in.html
# http://pyvideo.org/video/276/the-mighty-dictionary-55

import random

# In python 
# In hash table (initial 8 slots) store (hash,key,value)

class Pair:
	def __init__(self,key,value):
		self.key = key
		self.value = value

	def get_value(self):
		return self.value

	def get_key(self):
		return self.key

class Hash:

	def __init__(self):
		self.tablesize = 20
		self.list = [[] for i in range(self.tablesize) ]
		pass

	def hash_function(self,key):
		index = 0
		for s in key:
			index += ord(s)
		return index % self.tablesize


	def get_value(self,key):
		index = self.hash_function(key)
		array = self.list[index]
		if len(array) == 0:
			print "There is no such key"
			return None
		else:
			for i,k in enumerate(array):
				if k.get_key() == key:
					return array[i].get_value()
			if i == len(array)-1 and array[i].get_key() != key:
				print "There is no such key"
				return None		

	def __getitem__(self,key):
		return self.get_value(key)
	
	# check is such key is already there
	# if not, insert
	# if yes, replace
	def set_pair(self,key,value):
		# turn key into string
		key = str(key)
		# calculate index
		index = self.hash_function(key)
		array = self.list[index]
		# check if array at this index is empty
		if len(array) == 0:
			array.append(Pair(key,value))
		# check is such key is already there
		else:
			for i in range(len(array)):
				# if exist, replace
				if array[i].get_key() == key:
					array[i] = Pair(key,value)
					break			
			# If doesn't exist, append at end
			if i == len(array) - 1 and array[i].get_key() != key:
				array.append(Pair(key,value))



	def keys(self):
		s = ""
		for a in self.list:
			if len(a) > 0:
				for b in a:
					s += b.get_key() + " "
		return s


	def __str__(self):
		s = ""
		for a in self.list:
			if len(a) > 0 :
				s += a[0].get_key() + " "
		return s



h = Hash()
#print h.list
#h.set_pair("ala","kota")
#h.set_pair("benoit","kota")
#h.set_pair(123,"kota")

s = ""
for i in range(100):
	k =  chr(random.randrange(48,122))
	h.set_pair(k,i)
	s += k + " "
	
print h.keys()
print s



