n = int(input("Enter an Integer: "))

def fib(n): 
    x = 0
    y = 1
    if (n < 1):
        return
    for i in range(0, n):
        print(y, " ")
        next = x + y
        x = y
        y = next
         
fib(n)