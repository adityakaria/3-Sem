import math

class PriorityQueue:
	def __init__(self, array=None):
		
		if array is None:
			self.elements = []
			self.n = 0
		else:
			self.elements = array
			self.n = len(self.elements)
			self.elements = self.buildHeap(self.elements)
		

	def show(self):
		print(self.elements)
		print("n: ", self.n)

	def heapify(self, a, i):
		if ((2*i)) > self.n:
			print("------1-------")
			return a

		if ((2*i)+1) <= self.n:
			r = a[(2*(i))]
		else:
			r = -9999999
		l = a[2*(i)-1]
		c = a[i-1]

		print("l, c, r, i = ", l, c, r, i)
		if (c < l) or (c < r):
			if l > r:
				p= (2*i -1)
				if p == 0:
					p = 2
				print("--------2a-------", p)
			elif l < r:
				p = (2*i)
				if p == 0:
					p = 1
				print("--------2b-------", p)
			else:
				print("--------2c-------")
				return
			a[i-1], a[p] = a[p], a[i-1]
			print("new heap:", self.elements)
			a = self.heapify(a, p+1)
		else:
			print("--------3-------")
			return a

	def max(self):
		return self.elements[0]

	def extractMax(self):
		print("extracting max...")
		print(self.elements)
		self.elements[0] = self.elements[self.n -1]
		print(self.elements)
		del self.elements[self.n -1]
		print(self.elements)
		self.elements = self.heapify(self.elements, 1)

	def buildHeap(self, array):
		print("-----------", array, self.n, math.floor((self.n)/2))
		for i in range(math.floor((self.n)/2), 0, -1):
			print("-----------", array, i)
			print("heapifying while building---------------------------")
			self.heapify(array, i)
		return array

	def insert(self, x):
		a = self.elements
		self.n += 1
		i = self.n
		print("inserting", x, "i =", i+1)
		a.append(x)
		while (a[i-1] > a[math.floor((i-1)/2)]):
			a[math.floor((i-1)/2)], a[i-1] = a[i-1], a[math.floor((i-1)/2)]
			print("-----")
			i = math.floor((i-1)/2)

def main():
	test_array = [1,4,5,0,9, 7]
	q = PriorityQueue(test_array)

	q.show()
	q.insert(6)
	q.show()
	q.insert(-4)
	q.show()

	print("max: ", q.max)
	q.show()
	q.extractMax()
	q.show()

if __name__ == '__main__':
	main()