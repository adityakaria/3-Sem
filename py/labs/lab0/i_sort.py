a = [4, 6, 7, 2, 0, 22, 69, 9, 10, 3, -1, 5]

print("The following program represents insertion sort:")

print("Before:	", a)

for i in range(1, len(a)):
	k = i
	for j in range(i - 1, -1, -1):
			if a[k] < a[j]:
				temp = a[k]
				a[k] = a[j]
				a[j] = temp
			k -= 1


print ("After:	",a)