"""Stacks and queues
Author: Aditya karia
Date: July, 2018"""

class node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class stack:
	def __init__(self):
		self.top = None

	def push(self, data): 
		"""Adds element to top of queue"""
		cur = node(data)
		if self.top == None:
			self.top = cur
		else:
			temp = self.top
			self.top = cur
			cur.next = temp
		print ("push successful")

	def pop(self):
		if self.top == None:
			print ("Stack Empty\nOpereation Failed")
			return None
		else:
			x = self.top.data
			temp = self.top
			temp = temp.next
			self.top = temp
			return x

	def peek(self):
		if self.top == None:
			print ("Stack Empty")
			return None
		else:
			temp = self.top
			print ("top element is", temp.data)
			return temp.data

	def s_len(self):
		leng = 0
		cur = self.top
		while cur != None:
			cur = cur.next
			leng += 1
		print ("length is", leng)

	def s_display(self):
		elem = []
		cur = self.top
		if cur == None:
			print (elem)
		else:
			while cur != None:
				elem.append(cur.data)
				cur = cur.next
			print (elem)


class queue:
	def __init__(self):
		self.q1 = stack()
		self.q2 = stack()

	def enqueue(self, data):
		self.q1.push(data)

	def dequeue(self):
		if self.q1.s_len() == 0:
			print ("queue empty")
		elif self.q1.s_len() == 1:
			x = self.q1.pop()
			print(x, "is dequeued\nand the queue is now empty")
			return x
		else:
			q2 = stack()
			while self.q1.s_len != 0:
				x = self.q1.pop()
				self.q2.push(x)
			x = self.q2.pop()
			print (x, "is dequeued")
			while self.q2.s_len != 0:
				x = self.q1.pop()
				self.q1.push(x)
	
	def front(self):
		if self.q1.s_len() == 0:
			print ("queue empty")
		elif self.q1.s_len() == 1:
			x = self.q1.peek()
			print(x, "is in front")
			return x
		else:
			cur = self.q1.top
			while cur.next != None:
				cur = cur.next
			x = cur.data
			print(x, "is in front")
			return x

	def q_dis(self):
		self.q1.s_display()


Test = queue()

Test.q_dis()
Test.enqueue(5)
Test.enqueue(9)
Test.enqueue(25)

Test.q_dis()

Test.front()
Test.dequeue()

Test.q_dis()

Test.front()
Test.dequeue()


Test.q_dis()

Test.front()