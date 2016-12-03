class Graph:
	nodes = {} #allows node to be found by name
	
	def addnode(self, node):
		if isinstance(node, Node) and node.name not in self.nodes: #checks if node exists and does not exist in nodes dictionary
			self.nodes[node.name] = node #adds node to nodes dictionary
			return True
		else:
			return False
	
	def addedge(self, w, v):
		if w in self.nodes and v in self.nodes: #checks if edge is in dictionary
			self.nodes[w].add_sibling(v)
			self.nodes[v].add_sibling(w)
			return True
		else:
			return False
			
	def result(self): #function to print the result
		for key in sorted(list(self.nodes.keys())):
			print(key + str(self.nodes[key].siblings))

class Node:
	def __init__(self, n):
		self.name = n
		self.siblings = list()
	
	def add_sibling(self, v):
		if v not in self.siblings:
			self.siblings.append(v) #appends node to list
			self.siblings.sort() #sorts the list

g = Graph()
a = Node('A')
g.addnode(a)
g.addnode(Node('B'))
for i in range(ord('A'), ord('K')):
	g.addnode(Node(chr(i)))

edges = ['FG', 'FJ', 'GA', 'HB', 'IJ', 'IC', 'JC', 'AB', 'FD', 'AE', 'BE', 'CD']
for edge in edges:
	g.addedge(edge[:1], edge[1:])

g.result()
