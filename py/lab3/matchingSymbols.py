from mystack import Stack

def invert(symbol):
	if symbol == '}':
		symbol = '{'
	elif symbol == ']':
		symbol = '['
	elif symbol == ')':
		symbol = '('
	return symbol

def isMatched(expr):
    """Checks if the expression 'expr' has matching opening/closing symbols."""

    s = Stack()
    for char in expr:
    	if char == '[' or char == '{' or char == '(':
    		s.push(char)
    	elif char == ']' or char == '}' or char == ')':
    		if s.isEmpty():
    			return False
    		else:
    			symbol = s.peek()
    			char = invert(char)

    			if symbol == char:
    				s.pop()
    			else:
    				return False

    if s.isEmpty():
    	return True
    else:
    	return False




def main():
	expr = input('Enter the expression: ')
	if isMatched(expr):
		print('Matched symbols')
	else:
		print('Unmatched symbols')

if __name__ == '__main__':
    main()
