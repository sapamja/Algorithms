# Dome info about operations in heap
# http://en.wikipedia.org/wiki/Binary_heap

import math

class Heap:
	def __init__(self):
		self.heap = []

	def parent(self,i):
		p = math.floor((i-1)/2)
		if p >= 0:
			return int(p)
		else:
			return None

	def children(self,i):
		return [2*i+1,2*i+2] 

	def add_item(self,item):
		self.heap.append(item)
		i = len(self.heap)-1
		p = self.parent(i)
		while p != None and self.heap[i] > self.heap[p]:
			self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
			i = self.parent(i)
			p = self.parent(i)

	# Breadth first search
	def bfs(self,item):
		i = 0
		while i <= len(self.heap):
			if self.heap[i] == item:
				return i
			else:
				i += 1

	def dfs(self,i,item):
		print i,self.heap[i]
		if self.heap[i] == item:
			print "here"
			return i
		else:
			if 2*i+1 < len(self.heap):
				print "here left",i,2*i+1
				return self.dfs(2*i+1,item)
		
			if 2*i+2 < len(self.heap):
				print "here right",i,2*i+2
				return self.dfs(2*i+2,item)

	def __str__(self):
		return str(self.heap)


h = Heap()
h.add_item(5)
h.add_item(20)
h.add_item(10)
h.add_item(15)
h.add_item(40)
h.add_item(50)
print h

#print h.bfs(15)
print h.dfs(0,15)




