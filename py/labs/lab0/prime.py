n = int(input("Enter a number: "))

flag = 0
for i in range(n-1, 1, -1):
	if (n % i == 0):
		print("The number is non-prime")
		flag = 1
		break

if flag == 0:
	print("The number is prime")