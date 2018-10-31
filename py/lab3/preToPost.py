from mystack import Stack
from postfixEval import eval_postfix

def toPost(p):
	s = Stack()
	q = []
	p = p.split()

	for i in reversed(p):
		if (operator(i) == False):
			s.push(i)
		else:
			a = s.pop()
			b = s.pop()

			s.push(str(a + ' ' +  b + ' ' + i))
			q = str(a + ' ' +  b + ' ' + i)


	q = ''.join(q)
	return q



def operator(i):
	if i == '+' or i == '-' or i == '*' or i == '/' or i == '%':
		return True
	return False


def main():
	a = input("Enter prefix expression: ")
	r = toPost(a)
	print("--1--")
	print(r)
	print("--2--")
	print("Evaluated to ", eval_postfix(r))

if __name__ == '__main__':
	main()