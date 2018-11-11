from hashTable import HashTable

def main():
	table = HashTable(30)

	choice = int(input("Choose dictionary to use:\n1. small.dict\n2. ispell.dict\n9. Exit\n"))
	if choice == 1:
		f = open("small.dict", "r")
	elif choice == 2:
		f = open("ispell.dict", "r")
	elif choice == 9:
		return 0


	a = f.read().splitlines()
	print("Loading dictionary. Please wait...\n")
	for word in a:
		table.insert(word)
	print("Ready! Please enter values...")
	while True:
		key = input("Enter element to search: (Enter k to exit)\n")
		if key == 'k':
			break
		else:
			table.search(key)


if __name__ == '__main__':
	main()