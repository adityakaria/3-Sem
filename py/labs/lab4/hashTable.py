from ll import ll

class HashTable:
	def __init__(self, m):
		self.size = m
		self.T = [ll() for i in range(m)]
		self.choice = int(input("\nPlease Enter choice:\n1)Component Sum\n2)Horner's [polynomial accumulation]\n"))
		if self.choice != 1:
			self.x = int(input("What is the coefficient for polynomial accumulation?\n"))
		print("")

	def hashit(self, key):
		if self.choice == 1:
			hashed = 0
			for i in key:
				hashed += ord(i)

			hashed %= self.size
			return hashed

		elif self.choice == 2:
			if key != "":
				i = key[0]
				hashed = ord(i) + (self.x * self.hashit(key[1:]))
			else:
				return 0
			return hashed

		else:
			print("using polynomial accumulation")
			if key != "":
				i = key[0]
				hashed = ord(i) + (self.x * self.hashit(key[1:]))
			else:
				return 0
			return hashed



	def insert(self, key):
		hashed = self.hashit(key)
		hashed %= self.size
		self.T[hashed].insert(hashed, key, 0)

	def displayAll(self):
		for i in range(0, self.size):
			print(i, ': ', end='	')
			self.T[i].display()
			print("")
		print("")

	def search(self, key):
		hashed = self.hashit(key)
		hashed %= self.size

		k = self.T[hashed].getIndexKey(key)
		if k != None:
			# print("Element '" + key + "' found\nIndex: ", hashed, "	Position: ", k)
			print("Element found. Word is valid")
			# print(" = = \n\\___/\n")
			print("")
		else:
			print("Element not found. Invalid word")
			print("\nDid you mean any of these?")
			self.autocorrect(key)
			# print("\n\\  /\n \\/\n /\\\n/  \\\n")
			self.insauto(key)
			self.delauto(key)
			print("")

	def keys(self):
		print("Keys present in the table are:")
		print("Hash\tKey")
		for i in range(0, self.size):
			self.T[i].printKeys()
		print()

	def autocorrect(self, key):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'

		for i in range(0,len(key)):
			for k in alphabet:
				hashed = self.hashit((key[0:i] + k + key[i+1:]))
				hashed %= self.size
				v = self.T[hashed].getIndexKey((key[0:i] + k + key[i+1:]))
				if v != None:
					print((key[0:i] + k + key[i+1:]))
				else:
					pass
	
	def insauto(self, key):
		for i in range(0, len(key)):
			key1 = key[:i] + 'x' + key[i:]
			self.autocorrect(key1)

	def delauto(self, key):
		for i in range(0, len(key)):
			key1 = key[:i] + key[i+1:]
			self.autocorrect(key1)




def main():
	m = int(input("what is the size of table? "))
	table = HashTable(m)
	# cont = 'y'
	while True:
		choice = int(input("\nChoose your operation: \n1. Display hashtable\n2. Insert elements\n3. Show all keys present in table\n4. Search for a key in table\n9. Exit\n"))
		print("")
		if choice == 1:
			table.displayAll()

		elif choice == 2:
			print("You can now enter elements one-by-one.\nIn case you are done, just enter k (to kill operation")
			while True:
				read = input("Enter Element: ")
				if read == 'k':
					break
				else:
					table.insert(read)
		elif choice == 3:
			table.keys()
		elif choice == 4:
			key = input("Enter key to search: ")
			table.search(key)
		elif choice == 9:
			break




if __name__ == '__main__':
	main()
