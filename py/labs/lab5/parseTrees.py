class TreeNode:
	
	def __init__(self,value=None,left=None,right=None,parent=None):
		self.value=value
		self.left=left
		self.right=right
		self.parent=parent

	def inOrder(self):
	    s=""
	    if self.left is not None:
	        s+=self.left.inOrder()
	    s+=self.value
	    if self.right is not None:
	        s+=self.right.inOrder()
	    return s

class ParseTree:

	def __init__(self):
		self.root=None

	def build(self,exp):
		l=list(exp)
		t=TreeNode()
		operators=['+','-','*','/']
		for i in l:
			if i is '(':
				t.left=TreeNode(None,None,None,t) # makes a left node and goes to in
				t=t.left
			elif i in operators:
				t.value=i						#if operator, then make cur.value=operator, and the next value should be cur.right, so go there
				t.right=TreeNode(None,None,None,t)
				t=t.right
			elif i is ')':						#go to parent
				t=t.parent if t.parent is not None else t
			else:
				t.value=i
				t=t.parent if t.parent is not None else t

		while t.parent is not None:
			t=t.parent
		self.root=t

	def equation(self):
		return self.root.inOrder()

def pre_trav(node):
	curr=node
	if(curr!=None):		
		print(curr.value,"",end="")
		pre_trav(curr.left)
		pre_trav(curr.right)
	else:
		return

def post_trav(node):
	curr=node
	if(curr!=None):		
		post_trav(curr.left)
		post_trav(curr.right)
		print(curr.value,"",end="")
	else:
		return

def main():
	s=input("Enter your Equation: ")
	p=ParseTree()
	p.build(s)
	print(p.equation())

	print("pre-order traversal: ")
	pre_trav(p.root)
	print()

	print("post-order traversal: ")
	post_trav(p.root)
	print()

	print("Value of expression: ", end=" ")
	print(eval(s))


if __name__=='__main__':
	main()
