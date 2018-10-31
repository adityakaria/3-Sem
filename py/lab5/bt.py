class node:
	def __init__(self, data = None, parent = None):
		self.data = data
		self.right = None
		self.left = None
		self.parent = parent

class bt:
	def __init__(self):
		self.root = None

	def insert(self, data):
		temp = node(data)
		if self.root is None:
			self.root = temp
			return self.root
		
		cur = self.root
		while data != cur.data:			
			if data > cur.data:
				if cur.right != None:
					cur = cur.right
				else:
					cur.right = temp
					temp.parent = cur
					break
			elif data < cur.data:
				if cur.left != None:
					cur = cur.left
				else:
					cur.left = temp
					temp.parent = cur
					break
		return cur

	def inorder(self, node):
		cur = node
		if cur.left != None:
			self.inorder(cur.left)
		print (cur.data)
		if cur.right != None:
			self.inorder(cur.right)

	def search(self, value):
		if self.root is None:
			print("Tree empty. Search failed")
			return None
		cur = self.root
		if self.root.data == value:
			print("Element found", value)
			return cur

		while (cur is not None) and (cur.data != value):
			if (value < cur.data):
				cur = cur.left
			elif value > cur.data:
				cur = cur.right
		if cur is not None and cur.data == value:
			print("Element found", value)
			return cur
		else:
			print("Element not found", value)
			return None

	def max(self, node):
		cur = node
		if cur is None:
			print("ERROR: Tree empty\nOperation failed")
			return None
		else:
			while cur.right != None:
				cur = cur.right
			# print("MAX Element is ", cur.data)
			return cur

	def min(self, node):
		cur = node
		if cur is None:
			print("ERROR: Tree empty\nOperation failed")
			return None
		else:
			while cur.left != None:
				cur = cur.left
			# print("MIN Element is ", cur.data)
			return cur

	def successor(self, value):
		cur = self.search(value)
		if cur is None:
			return None
		elif cur.right is not None:
			return self.min(cur.right).data
		else:
			while cur.parent != None and cur == cur.parent.right:
				cur = cur.parent
			if cur.parent is None:
				print(value, " is max Element")
				return
			elif cur.parent is not None and cur == cur.parent.left:
				return cur.parent.data

	def predecessor(self, value):
		cur = self.search(value)
		if cur is None:
			return None
		elif cur.left is not None:
			return self.max(cur.left).data
		else:
			while cur.parent != None and cur == cur.parent.left:
				cur = cur.parent
			if cur.parent is None:
				print(value, " is min Element")
				return
			elif cur.parent is not None and cur == cur.parent.right:
				return cur.parent.data

	def delete(self, value):
		
		cur = self.search(value)

		if cur is None:
			return None
		
		elif cur.left is None and cur.right is None: #if leaf
			if cur == cur.parent.right:
				cur.parent.right = None
			elif cur == cur.parent.left:
				cur.parent.left = None

		elif cur.left is None or cur.right is None:  #if one child
			print("--2--")
			
			if cur == cur.parent.right:
				if cur.left is not None:
					cur.parent.right = cur.left
				elif cur.right is not None:
					cur.parent.right = cur.right

			elif cur == cur.parent.left:
				if cur.left is not None:
					cur.parent.left = cur.left
				elif cur.right is not None:
					cur.parent.left = cur.right

		else:
			print("--3--")
			m = self.min(cur.right)

			temp = cur.data
			cur.data = m.data
			m.data = temp

			m.parent.left = None


		print("Element deleted: ", value)



def main():
	tree = bt()
	tree.insert(2)
	tree.insert(4)
	tree.insert(1)
	tree.insert(9)
	tree.insert(5)
	tree.insert(3)
	tree.insert(6)

	tree.inorder(tree.root)

	tree.search(6)
	tree.search(88)

	print("max: ", tree.max(tree.root).data)
	print("min: ", tree.min(tree.root).data)

	print("successor: ", tree.successor(2))
	print("successor: ", tree.successor(5))
	print("predecessor: ", tree.predecessor(9))
	print("predecessor: ", tree.predecessor(1))

	tree.delete(6)
	tree.inorder(tree.root)

	tree.delete(88)
	tree.inorder(tree.root)


if __name__=='__main__':
	main()