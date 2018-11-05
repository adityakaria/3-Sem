"""Linked list
Date: 30 June, 2018"""

class node:
	def __init__(self, data = None):
		self.data = data
		self.prev = None
		self.next = None

class ll:
	def __init__(self):
		self.head = node()

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node
		new_node.prev = cur

	def insert(self, data, index):
		temp = node(data)
		cur = self.head
		for i in range(index):
			cur = cur.next
		temp.next = cur.next
		cur.next = temp
		
	def length(self):
		length = 0
		cur = self.head
		while cur.next != None:
			cur = cur.next
			length += 1
		return length

	def display(self):
		elem = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elem.append(cur.data)
		print (elem)

	def del_ind(self, index):
		if index >= self.length():
			print ("ERROR:\nIndex out of Range")
			return None
		else:
			cur = self.head
			for i in range(0, index):
				cur = cur.next
			prev = cur
			cur = cur.next
			prev.next = cur.next

	def get_data(self, index):
		if index >= self.length():
			print ("ERROR:\nIndex out of Range")
			return None
		else:
			cur = self.head
			for i in range(0, index + 1):
				cur = cur.next
			print ("Value at index", index, "is", cur.data)
	
	def get_index(self, data):
		cur = self.head
		cur = cur.next
		index = 0
		flag = 0
		for i in range(self.length()):
			if cur.data != data:
				cur = cur.next
				index += 1
			elif cur.data == data:
				flag = 1
				print ("First index of value", data, "is", index)
				break
			
		if flag== 0:
			print("Element " + str(data) + " not found")		

def main():
	lis = ll()

	lis.display()
	lis.append(4)
	lis.append(5)
	lis.append(21)
	lis.display()
	print ("list length =", lis.length())
	lis.insert(9, 1)
	lis.display()
	lis.get_index(21)
	lis.get_data(0)
	lis.display()
	lis.get_index(5)
	lis.del_ind(0)
	lis.display()
	lis.get_index(5)

if __name__ == '__main__':
	main()