n = int(input("Enter Integer 1: "))
m = int(input("Enter Integer 2: "))

def larger(x, y):
	if x > y:
		return x
	else:
		return y

def gcd(x, y):
	for i in range(larger(x,y), 0, -1):
		if (x % i ==  0) and (y % i == 0):
			return i
	return 1

print(gcd(m, n))