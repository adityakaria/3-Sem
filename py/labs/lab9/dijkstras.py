from MinHeapNodes import MinHeap
from MinHeapNodes import Edge

class Node:
	def __init__(self, name):
		self.name = name
		self.adj = []
		self.color = 'white'
		self.st = None
		self.et = None
		self.parent = None
		self.string = ""
		self.dist = 9999999
		self.pred = None
		self.edgesFrom = []

	def __str__(self):
		return(str(self.name) + ": " + str(self.dist))

	def __eq__(self, other):
		if other is None:
			return None
		return self.dist == other.dist

	# def __ne__(self, other):
	# 	return self.dist != other.dist

	def __le__(self, other):
		return self.dist <= other.dist

	def __lt__(self, other):
		return self.dist < other.dist

	def __ge__(self, other):
		return self.dist >= other.dist

	def __gt__(self, other):
		return self.dist > other.dist
 

class Graph:
	def __init__(self):
		self.nodes = []
		self.edges = []
		self.time = 0

	def checkedge(self, node1, node2):
		for i in node1.adj:
			if node2.name == i.name:
				return 1
		return 0
	
	def insert(self, name):
		name = name.split()
		if len(name) == 3:
			neighbour = int(name[1])
		else:
			neighbour = None

		weight = name[2]
		name  = int(name[0])
		self.edges.append(Edge(name, neighbour, weight))
		
		flag = 0
		for i in self.nodes:
			if name == i.name:
				temp = i
				flag = 1
				break
		if flag == 0:
			temp = Node(name)
			self.nodes.append(temp)
		
		flag = 0
		if neighbour != None:
			for i in self.nodes:
				if neighbour == i.name:
					temp2 = i
					flag = 1
					break
			if flag == 0:
				temp2 = Node(neighbour)
				self.nodes.append(temp2)
			
			temp.adj.append(temp2)

		temp.edgesFrom.append(Edge(name, neighbour, weight))
		

	def __str__(self):
		string = ""
		if len(self.nodes) == 0:
			return "Graph Empty\n"
		print("Adjacency List: ")
		for i in self.nodes:
			string += str(i.name) + ": ["
			for j in i.adj:
				string += str(j.name) + ", "
			string += "\b" + "\b" + "]\n"
		return string
	
	def adjacency_matrix(self):
		print("Adjacency Matrix:")
		for i in self.nodes:
			row = [0] * (len(self.nodes))
			for j in i.adj:
				row[j.name] = 1
			print(str(i.name) + ": ", end=" ")
			for i in row:	
				print(i, end=" ")
			print()

	def findNode(self, u):
		flag = 0
		for i in self.nodes:
			if i.name == u:
				return i
		print("Node not found")
		return None

	def dfs(self, u):
		if u == None:
			print("ERROR: Node empty")
			return
		u.color = 'grey'
		self.time += 1
		u.st = self.time
		u.string += str(u.name) + " [" +  str(u.st)
		for v in u.adj:
			if v.color == 'white':
				self.dfs(v)
				v.parent = u
		u.color = "black"
		self.time += 1
		u.et = self.time
		u.string += ", " + str(u.et) + ']'
		

	def dijkstras(self, s):
		s = self.findNode(s)
		if s == None:
			print("ERROR: Source not valid")
			return
		for u in self.nodes:
			u.dist = 9999999
			u.pred = None

		s.dist = 0
		H = MinHeap()
		for u in self.nodes:
			H.insert(u)


		while (H.isEmpty() is False):
			w = H.extractMin()
			for v in w.adj:
				for k in w.edgesFrom:
					if v.name == k.end:
						destination = k
				if v.dist > w.dist + destination.weight:
					v.dist = w.dist + destination.weight
					H.updatePriority(v, v.dist)
					v.pred = w
				no = v
				v = self.findNode(v.name)
				v = no

		for u in self.nodes:
			print(u.name, ": ", u.dist)

		print()
		print("Path: ")
		for i in self.nodes:
			print(i.name, end=" -> ")
			n = i
			while n.pred != None:
				print(n.pred.name, end=" -> ")
				n = n.pred
			print("\b\b\b     ")

def main():
	g= Graph()
	print(g)
	# g.insert('a', ['b', 'c'])
	# g.insert('b', ['a', 'e', 'd'])
	# g.insert('c', [])
	# g.insert('a', 'b')
	# g.insert('b')
	n = int(input("Number of edges: "))
	for i in range(n):
		g.insert(input())
	# g.insert("0 1")
	# g.insert("0 2")
	# g.insert("1 2")
	# g.insert("1 3")
	# g.insert("1 4")
	# g.insert("2 3")
	print(g)
	g.adjacency_matrix()
	print()
	print()
	print()
	p = int(input("Enter source vertex: "))
	g.dijkstras(p)
	

if __name__ == '__main__':
	main()
