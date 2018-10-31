from mystack import Stack
from postfixEval import evaluate

def toPost(p):
	s = Stack()
	q = []
	p = p.split()

	for i in reversed(p):
		if (operator(i) == False):
			s.push(int(i))
		else:
			a = s.pop()
			b = s.pop()

			s.push(evaluate(a, i, b))

	return s.pop()



def operator(i):
	if i == '+' or i == '-' or i == '*' or i == '/' or i == '%':
		return True
	return False


def main():
	a = input("Enter prefix expression: ")
	print(toPost(a))

if __name__ == '__main__':
	main()