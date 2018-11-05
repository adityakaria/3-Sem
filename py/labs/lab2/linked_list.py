class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    def insert(self,x,pos):
        """Insert element x in the position after pos"""
        new = ListNode()
        new.value = x
        new.next = pos.next
        pos.next = new

    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        pos.next = pos.next.next

    def print(self):
        """ Print all the elements of a list in a row."""
        temp = self.head
        while temp.next!=None:
            temp = temp.next
            
            print(temp.value, end= ' ')
        print("")

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp = self.head

        for j in range(0,i):
            if temp.next==None:
                return 1
            temp = temp.next

        new = ListNode()
        new.value = x
        new.next = temp.next
        temp.next = new


    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp = self.head

        while temp.next != None:
            if (x == temp.value):
                print("Found")
                return temp       
            temp = temp.next

        print("Not Found")


    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        count = 0
        temp = self.head
        while temp.next!=None:
            count += 1
            temp = temp.next
        return(count)

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next == None:
            return True
        return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    print('List is: ')
    L.print()
    L.insert(10,L.head)
    print('List is: ')
    L.print()
    L.insert(12,L.head.next)
    print('List is: ')
    L.print()
    L.insert(2,L.head)
    print('List is: ')
    L.print()
    print('Size of L is ',L.len())
    
    print("")
    print(L.search(2))
    print('List is: ')
    L.print()
    print(" ")
    
    L.delete(L.head)
    print('List is: ')
    L.print()
    L.delete(L.head.next)
    print('List is: ')
    L.print()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ')
    L.print()

if __name__ == '__main__':
    main()