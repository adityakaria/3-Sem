class TreeNode:
	def __init__(self,value=None,left=None,right=None,parent=None):
		self.value=value
		self.left=left
		self.right=right
		self.parent=parent

	def preOrder(self):
		print(self.value,end=" ")
		if self.left is not None:
			self.left.preOrder()
		if self.right is not None:
			self.right.preOrder()




class BST:
	def __init__(self,value,left=None,right=None):
		self.root=TreeNode(value,left,right)

	def search(self,value,node):
		if node is None:
			return None
		elif node.value==value:
			return node
		elif node.value<=value:
			return self.search(value,node.right)
		else:
			return self.search(value,node.left)

	def insert(self,value):
		t = self.root
		while True:
			if t.value<value:
				if t.right is None:
					temp = TreeNode(value,None,None,t)
					t.right = temp
					break
				else:
					t = t.right
			else:
				if t.left is None:
					temp = TreeNode(value,None,None,t)
					t.left = temp
					break
				else:
					t = t.left
	def print(self):
		self.root.preOrder()
		print()

	def minimum(self):
		t = self.root
		while t.left is not None:
			t = t.left
		return t.value

	def maximum(self):
		t = self.root
		while t.right is not None:
			t = t.right
		return t.value

	def successor(self,value):
		t = self.search(value,self.root)
		if t is not None:
			if t.right is not None:
				r = t.right
				while r.left is not None:
					r = r.left
				return r.value
			else:
				p = t.parent
				while p is not None and t is p.right:
					t = p
					p = p.parent
				if p is not None:
					return p.value
				else:
					return None
		else:
			print(value,"not present in BST")
			return

	def predecessor(self,value):
		t = self.search(value,self.root)
		if t is not None:
			if t.left is not None:
				l = t.left
				while l.right is not None:
					l = l.right
				return l.value
			else:
				p = t.parent
				while p is not None and t is p.left:
					t = p
					p = p.parent
				if p is not None:
					return p.value
				else:
					return None
		else:
			print(value,"not present in BST")
			return

	def delete(self,value,node):
		t = self.search(value,node)
		temp = None
		if t is not None:
			p = t.parent
			if t.right is None and t.left is not None:
				temp = t.left

			elif t.right is not None:
				s = self.search(self.successor(value),t.right)
				temp = s
				self.delete(s.value,t.right)
				
			if p is not None:
				if p.value<value:
					p.right = temp
				else:
					p.left = temp
			else:
				t.right.parent=temp
				t.left.parent=temp
				self.root=temp

			if temp is not None:
				temp.right = t.right
				temp.left = t.left
				temp.parent = p

def main():
	tree = BST(10)
	tree.insert(5)
	tree.insert(12)
	tree.insert(8)
	tree.insert(11)
	tree.print()
	print()
	print("Successor(8) :",tree.successor(8))
	print()
	print("predecessor(8) :",tree.predecessor(8))
	print()
	print("Minimum of tree is:",tree.minimum())
	print("Maximum of tree is:",tree.maximum())
	print()
	print("deleting 5: ")
	tree.delete(5,tree.root)
	tree.print()


if __name__=='__main__':
	main()
