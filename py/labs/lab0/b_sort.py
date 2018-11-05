a = [4, 6, 7, 2, 0, 22, 69, 21, 9, 3, 10]

print(a)

for i in range(len(a) - 1):
	for j in range(i + 1, len(a)):
		if a[i] > a[j]:
			temp = a[i]
			a[i] = a[j]
			a[j] = temp

print (a)