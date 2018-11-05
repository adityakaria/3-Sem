n = int(input("Enter a number: "))

def fact(n):
	if n <= 1:
		return 1
	else:
		return (n * fact(n-1))


print("The factorial of " + str(n) + " is: " + str(fact(n)))