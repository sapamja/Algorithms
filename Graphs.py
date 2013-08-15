# Graph
# http://docs.yworks.com/yfiles/doc/developers-guide/analysis.html
# * Breadth first search
# * Depth first search
# * Find if graph is connected
# * http://www.python.org/doc/essays/graphs.html


class Node:
	def __init__(self):
		self.edges = []
		self.seen = False
	
	def get_edges(self):
		return self.edges

	def add_edge(self,n):
		self.edges.append(n)

class Graph:
	def __init__(self):
		self.nodes = dict()

	def add_node(self,n):
		if n not in self.nodes.keys():
			self.nodes[n] = Node()
		else:
			pass
			#print "Node",n,"already exists"

	def add_edge(self,n1,n2):
		self.nodes[n1].add_edge(n2)

	def add_edges(self,n,list_of_edges):
		self.nodes[n].edges.extend(list_of_edges)

	def list_of_nodes(self):
		return self.nodes.keys()

	def get_node(self,n):
		return self.nodes[n]

	def get_edges(self,n):
		return self.nodes[n].get_edges()

	def reset_seen(self):
		for n in self.nodes.keys():
			self.nodes[n].seen = False

	def set_as_seen(self,n):
		self.nodes[n].seen = True

	def wasSeen(self,n):
		return self.nodes[n].seen

# Breadth first traversal
	def bft(self,start_node):
		q = [start_node]
		while len(q) > 0:
			n = q.pop(0) # <- would be better to use proper fifo queue
			for e in self.get_node(n).get_edges():
				if not self.wasSeen(e):
					q.append(e)
			if not self.wasSeen(n):
				print n,
				self.set_as_seen(n)
			
# Breadth first traversal
	def bft2(self,start_node):
		q = [start_node,'new line']
		level = 0
		while len(q) > 0:
			n = q.pop(0) # <- would be better to use proper fifo queue
			if n == "new line":
				level += 1
				if len(q) > 0:
					q.append('new line')
				print ""
			else:
				for e in self.get_node(n).get_edges():
					if not self.wasSeen(e):
						q.append(e)
			
				if not self.wasSeen(n):
					print n,
					self.set_as_seen(n)
	
	# Path between two nodes
	def find_path(self,start,end,path):
		path.append(start)
		#print start,end,path
		if start == end:
			return path
		
		if len(self.get_node(start).get_edges()) == 0:
			return None
		
		for n in self.get_node(start).get_edges():
			if n not in path:
				p = path[:]
				newpath = self.find_path(n,end,p)
				if newpath:
					return newpath

		return None
			#return None

	# Path between two nodes
	# This code is not clear to me!
	def find_all_paths(self,start,end,path):
		path = path + [start]
		#print start,end,path
		if start == end:
			return path
		
		if len(self.get_node(start).get_edges()) == 0:
			return []
		
		paths = []
		for n in self.get_node(start).get_edges():
			if n not in path:
				#p = path[:]
				newpaths = self.find_all_paths(n,end,path)
				for newpath in newpaths:
					paths.append(newpath)

		return paths


	def copy_graph(self):
		new_graph = Graph()
		for n in self.nodes.keys():
			new_graph.add_node(n)
			edges = self.get_edges(n)
			new_graph.add_edges(n,edges)
		return new_graph


gl = [['A','B'],
	 ['B','G'],
	 ['B','F'],
	 ['B','E'],
	 ['B','D'],
	 ['D','C'],
	 ['C','A'],
	 ['F','H'],
	 ['H','A'],
	 ['G','A']
	 ]

g = Graph()
for n in gl:
	g.add_node(n[0])
	g.add_node(n[1])
	g.add_edge(n[0],n[1])

f = g.copy_graph()





#print g.list_of_nodes()
#g.bft('B'),
#print "===="
#g.reset_seen()
#g.bft2('B')
#print g.find_path('B','A',[])
#f.bft2('B')
print f.find_all_paths('B','A',[])

