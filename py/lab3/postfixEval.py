from mystack import Stack

def eval_postfix(s):
    """Evaluates the postfix expression 's'."""
    stack = Stack()

    s = s.split()
    for i in s:
    	if operator(i) == False:
    		stack.push(int(i))
    	else:
    		b = stack.pop()
    		a = stack.pop()
    		result = evaluate(a, i, b)
    		stack.push(result)
    return stack.pop()

def operator(i):
	if i == '+' or i == '-' or i == '*' or i == '/' or i == '%':
		return True
	return False

def evaluate(a, i, b):
	if i == '+':
		return a + b
	elif i == '-':
		return a - b
	elif i == '*':
		return a * b
	elif i == '/':
		return a / b
	elif i == '%':
		return a % b

def main():
	expr = input('Enter the postfix expression: ')
	print('The value of the expression is',eval_postfix(expr))

if __name__ == '__main__':
    main()

