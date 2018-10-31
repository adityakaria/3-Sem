"""Linked list
Date: 30 June, 2018"""

class node:
	def __init__(self, data = None, key = None):
		self.data = data
		self.key = key
		self.next = None

class ll:
	def __init__(self):
		self.head = node()

	def append(self, data, key):
		new_node = node(data, key)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def insert(self, data, key, index):
		temp = node(data, key)
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
			elem.append((cur.data, cur.key))
		print (elem)

	def delInd(self, index):
		if index >= self.length():
			print ("ERROR:\nIndex out of Range")
			return None
		else:
			cur = self.head
			for i in range(0, index):
				cur = cur.next
			cur.next = cur.next.next

	def getData(self, index):
		if index >= self.length():
			print ("ERROR:\nIndex out of Range")
			return None
		else:
			cur = self.head
			for i in range(0, index + 1):
				cur = cur.next
			print ("At index", index, "; Value: ", cur.data, "; Key: ", cur.key)

	def getIndexData(self, data):
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
			print("Element " , data, " not found")

	def getIndexKey(self, key):
		cur = self.head
		cur = cur.next
		index = 0
		flag = 0
		for i in range(self.length()):
			if cur.key == key:
				flag = 1
				return i
				break
			else:
				cur = cur.next
				index += 1

		if flag== 0:
			return None

	def printKeys(self):
		if self.length() == 0:
			pass
		else:
			cur = self.head

			while cur.next != None:
				cur = cur.next
				print(str(cur.data) + ":	", cur.key)


def main():
	lis = ll()

	lis.display()
	lis.append("India", 4)
	lis.append("USA", 5)
	lis.append("Spain", 21)
	lis.display()
	print ("list length =", lis.length())
	lis.insert("Pakistan", 9, 1)
	lis.display()
	lis.getIndexData("Spain")
	lis.getData(0)
	lis.display()
	lis.getIndexKey(5)
	lis.delInd(0)
	lis.display()
	lis.getIndexKey(5)

if __name__ == '__main__':
	main()