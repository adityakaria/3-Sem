class queue:
	def __init__(self, m = None):
		self.MAX = m
		self.q = []
		self.front = -1
		self.rear = -1

	def isEmpty(self):
		if self.front == self.rear == -1:
			return True
		else:
			return False

	def enqueue(self, value):
		if self.isEmpty() == True:
			self.front, self.rear = 0, 0
			self.q.append(value)

		else:
			if (self.front + 1) % self.MAX == self.rear:
				self.new_queue()

			self.front = (self.front + 1) % self.MAX
			if self.front < self.rear:
				self.q[(self.front)] = value
			else:
				self.q.append(value)

	def display(self):
		if self.front >= self.rear:
			print(self.q[self.rear:self.front + 1])
		else:
			print(self.q[self.rear:] + self.q[:self.front])

	def dequeue(self):
		if self.isEmpty():
			print("ERROR: Queue is already empty. Dequeue failed")
			return None
		elif self.rear == self.front:
				temp = self.q[self.rear]
				self.rear, self.front = -1, -1
				return temp
		else:
				temp = self.q[self.rear]
				self.rear = (self.rear + 1) % self.MAX
				return temp

	def new_queue(self):
		r = queue(self.MAX*2)
		while self.isEmpty() != True:
			r.enqueue(self.dequeue())
		self.q = r.q
		self.front = r.front
		self.rear = r.rear
		self.MAX = r.MAX

def main():
	n = int(input("Size of queue?"))
	myq = queue(n)

	while True:
		try:
			choice = int(input("choose operation:\n1.enqueue\n2.dequeue\n3.display\n4.clear queue\n9.quit\nEnter choice: "))
		except ValueError:
			print("Invalid input. Please enter only integers")
			try:
				choice = int(input("\nEnter choice: "))
			except ValueError:
				print("You are stupid. I quit")
				choice = 9

		if choice == 9:
			break

		if choice == 1:
				temp = input("Enter elements: (k to stop):")
			while (temp != 'k'):
				try:
					myq.enqueue(int(temp))
				Except ValueError:
					print("Invalid input.Integers only allowed.\nPlease try again:")
				temp = (input("Next element: "))
				if temp == 'k':
					break

		elif choice == 2:
			myq.dequeue()

		elif choice == 3:
			print("\nqueue is ", end="")
			myq.display()
			print("max = ", myq.MAX)
			print("")

		elif choice == 4:
			while True:
				if (myq.dequeue() == None):
					myq.MAX = n
					break



if __name__ == '__main__':
	main()




