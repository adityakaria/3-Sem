class Node:
	def __init__(self, name):
		self.name = name
		self.adj = []
		self.color = 'white'
		self.st = None
		self.et = None
		self.parent = None
		self.string = ""

	def __str__(self):
		return(self.name)

class Graph:
	def __init__(self):
		self.nodes = []
		self.time = 0

	def checkedge(self, node1, node2):
		for i in node1.adj:
			if node2.name == i.name:
				return 1
		return 0
	
	def insert(self, name):
		name = name.split()
		if len(name) == 2:
			neighbour = int(name[1])
		else:
			neighbour = None
		name  = int(name[0])
		
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
					i.adj.append(temp)
					temp2 = i
					flag = 1
					break
			if flag == 0:
				temp2 = Node(neighbour)
				temp2.adj.append(temp)
				self.nodes.append(temp2)
			
			temp.adj.append(temp2)
		

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
		print(u.name)
		for v in u.adj:
			if v.color == 'white':
				self.dfs(v)
				v.parent = u
		u.color = "black"
		self.time += 1
		u.et = self.time
		u.string += ", " + str(u.et) + ']'
		





def main():
	g= Graph()
	print(g)
	# g.insert('a', ['b', 'c'])
	# g.insert('b', ['a', 'e', 'd'])
	# g.insert('c', [])
	# g.insert('a', 'b')
	# g.insert('b')
	n = int(input("Number of edges: "))
	for i in range(n+1):
		g.insert(input())
	# g.insert("0 1")
	# g.insert("0 2")
	# g.insert("1 2")
	# g.insert("1 3")
	# g.insert("1 4")
	# g.insert("2 3")
	print(g)
	g.adjacency_matrix()
	



if __name__ == '__main__':
	main()
