import time



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
		flag = 0
		if self.root.data == value:
			return cur

		while (cur is not None) and (cur.data != value):
			if (value < cur.data):
				cur = cur.left
			elif value > cur.data:
				cur = cur.right
		if cur is not None and cur.data == value:
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
			m = self.min(cur.right)

			temp = cur.data
			cur.data = m.data
			m.data = temp

			m.parent.left = None



class Node:
	def __init__(self, data = None, parent = None):
		self.data = data
		self.right = None
		self.left = None
		self.parent = parent
		self.height = 1

class avl:
	def __init__(self):
		self.root = None

	def insert(self, data, pointer=None):
		if self.root is None:
			cur = Node(data, None)
			self.root = cur
			return

		else:
			if pointer is None:
				return Node(data)
			elif pointer.data > data:
				pointer.left = self.insert(data, pointer.left)
				pointer.left.parent = pointer
			else:
				pointer.right = self.insert(data, pointer.right)
				pointer.right.parent = pointer


		pointer.height = 1 + max(self.getHeight(pointer.left), self.getHeight(pointer.right))

		balance = self.checkBalance(pointer)


		# Case 1 - Left Left
		if balance > 1 and data < pointer.left.data:
			if pointer == self.root:
				self.root = pointer.left
			return self.rightRotate(pointer)

		# Case 2 - Right Right
		if balance < -1 and data > pointer.right.data:
			if pointer == self.root:
				self.root = pointer.right
			return self.leftRotate(pointer)

		# Case 3 - Left Right
		if balance > 1 and data > pointer.left.data:
			pointer.left = self.leftRotate(pointer.left)
			if pointer == self.root:
				self.root = pointer.left
			return self.rightRotate(pointer)

		# Case 4 - Right Left
		if balance < -1 and data < pointer.right.data:
			pointer.right = self.rightRotate(pointer.right)
			if pointer == self.root:
				self.root = pointer.right
			return self.leftRotate(pointer)
		
		return pointer


			#insert order: 2 -> 4 -> 1 -> 9 -> 5 -> 3 -> 6

	def leftRotate(self, z):
		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):
		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		# Return the new root
		return y

	
	def checkBalance(self, pointer):
		n = self.getHeight(pointer.left) - self.getHeight(pointer.right)
		return n

	def getHeight(self, pointer = None):
		if pointer == None:
			return 0
		else:
			return pointer.height

	def preorder(self, node):
		cur = node
		print (cur.data)
		if cur.left != None:
			self.preorder(cur.left)
		if cur.right != None:
			self.preorder(cur.right)

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
			return cur

		while (cur is not None) and (cur.data != value):
			if (value < cur.data):
				cur = cur.left
			elif value > cur.data:
				cur = cur.right
		if cur is not None and cur.data == value:
			return cur
		else:
			print("Element not found", value)
			return None

	def maxx(self, node):
		cur = node
		if cur is None:
			print("ERROR: Tree empty\nOperation failed")
			return None
		else:
			while cur.right != None:
				cur = cur.right
			# print("MAX Element is ", cur.data)
			return cur

	def minn(self, node):
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
			return self.minn(cur.right).data
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
			return self.maxx(cur.left).data
		else:
			while cur.parent != None and cur == cur.parent.left:
				cur = cur.parent
			if cur.parent is None:
				print(value, " is min Element")
				return
			elif cur.parent is not None and cur == cur.parent.right:
				return cur.parent.data

	def delete(self, root, key): 

	# Step 1 - Perform standard BST delete 
		if not root:
			return root

		elif key < root.data:
			root.left = self.delete(root.left, key)

		elif key > root.data:
			root.right = self.delete(root.right, key) 

		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp

			elif root.right is None:
				temp = root.left
				root = None
				return temp

			temp = self.minn(root.right)
			root.data = temp.data
			root.right = self.delete(root.right, temp.data)

		# If the tree has only one node,
		# simply return it
		if root is None:
			return root

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.checkBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and self.getBalance(root.left) >= 0:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and self.getBalance(root.right) <= 0:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and self.getBalance(root.left) < 0:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root 

	



def main():
	n= int(input("Enter no.of keys: "))
	start_time = time.time()
	tree = avl()
		
	for i in range(n):
		tree.insert(i, tree.root)

	print("----------")
	# tree.preorder(tree.root)


	# tree.search(6)
	# tree.search(88)

	# print("max: ", tree.maxx(tree.root).data)
	# print("min: ", tree.minn(tree.root).data)

	# print("successor: ", tree.successor(2))
	# print("successor: ", tree.successor(5))
	# print("predecessor: ", tree.predecessor(9))
	# print("predecessor: ", tree.predecessor(1))

	# tree.inorder(tree.root)

	# tree.delete(tree.root, 6)
	# tree.inorder(tree.root)

	# tree.delete(tree.root, 88)
	# tree.inorder(tree.root)

	print("­­­ %s 	seconds ­­­avl insert----------------" % (time.time()-start_time))

	start_time = time.time()

	btree = bt()
	broot = btree.root
	for i in range(n):
		btree.insert(i)


	print("­­­ %s 	seconds ­­­bt insert-----------------" % (time.time()-start_time))

	print()
	print()
	print()
	print
	n= int(input("Enter key to search: "))	

	start_time = time.time()
	tree.search(n)
	print("­­­ %s 	seconds ­­­avl search-----------------" % (time.time()-start_time))
	start_time = time.time()
	btree.search(n)
	print("­­­ %s 	seconds ­­­bt search------------------" % (time.time()-start_time))

	print()
	print()
	print()
	print
	n= int(input("Enter key to delete: "))

	start_time = time.time()
	tree.delete(tree.root, n)
	print("­­­ %s 	seconds ­­­avl delete-----------------" % (time.time()-start_time))
	start_time = time.time()
	btree.delete(n)
	print("­­­ %s 	seconds ­­­bt delete------------------" % (time.time()-start_time))


	


if __name__=='__main__':
	main()