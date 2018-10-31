"""
Assignment No: 2
Author: Aditya Karia
"""

"""
1) The 'top' is equivalent to 'Head', and points to first node
2) The function anmes are suggestive of the operation:
	Stacks: (LIFO)
		push- adds an element to the top of stack
		pop- removes an element from top of stack
		peek- returns the value of top element
		stack_len- returns the number of elements in stack
	Queues: (FIFO)
		queue- adds an element to the rear of queue
		dequeue- removes an element from front of queue
		front- returns the value of front element
3) Function 'main' runs the driver for testing of code
"""

class Node:
    def __init__(self, data = None, nxt = None):

        self.value = data
        self.next = nxt



class Stack:

    def __init__(self):
        
        self.top = None
       
    def push(self, i):
        
        if self.top == None:
            self.top = Node(i)
        else:
            temp = Node(i, self.top)
            self.top = temp

    def pop(self):
        if self.top == None:
            return None
        else:
            x = self.top.value
            self.top = self.top.next
            return x


    def peek(self):
        if self.top == None:
            print('Empty')
        else:
            return self.top.value


    def stack_len(self):
        current = self.top
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length



class Queue:

    def __init__(self):
        self.queue = Stack()

    def enqueue(self, data):
        self.queue.push(data)


    def dequeue(self):

        if (self.queue.stack_len() == 0):
            print("Queue empty")

        elif (self.queue.stack_len() == 1):
            n = self.queue.pop()
            print(n, "element is Dequeued")

        else:
            n = self.queue.pop()
            self.dequeue()
            self.queue.push(n)
            print(n, "element is Dequeued")



    def front(self):
        

        if (self.queue.stack_len() == 0):
            print("The queue is empty")


        elif (self.queue.stack_len() == 1):
            n = self.queue.peek()
            print("The front element is", n)

        else:
            n = self.queue.pop()
            self.front()
            self.queue.push(n)
            print("The front element is", n)
        

def main():
    
    Test = Queue()

    Test.enqueue(5)
    Test.enqueue(9)
    Test.enqueue(25)


    Test.front()
    Test.dequeue()

    Test.front()
    Test.dequeue()

    Test.front()


if __name__ == '__main__':
    main()


