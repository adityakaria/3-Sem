class Stack:
	"""Define the Stack class here.
	   Write a constructor and implement the push, pop and isEmpty functions
	   using Python lists.
	"""
	def __init__(self):
		self.my_stack = []
		self.top = -1

	def push(self, x):
		self.my_stack.append(x)
		self.top += 1
		print ("Push Successful\nThe stack now is: " + str(self.my_stack))

	def pop(self):
		popped = self.my_stack[self.top]
		self.my_stack.pop(self.top)
		self.top -= 1
		print("Popped", popped, "\nThe stack is now: ", self.my_stack)
		return popped

	def isEmpty(self):
		if (len(self.my_stack) == 0):
			return True
		else:
			return False

	def peek(self):
		print("The top element is: ", self.my_stack[self.top])
		return self.my_stack[self.top]

def main():
	s = Stack()
	s.push(1)
	s.push(9)
	s.push(69)
	s.pop()
	s.peek()
	print("isEmpty: ", s.isEmpty())

if __name__ == "__main__":
	main()