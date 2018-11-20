

class Edge:
    def  __init__(self,start, end, weight):
        self.weight = int(weight)
        self.start = int(start)
        self.end = int(end)

    def __eq__(self, other):
        if other is None:
            return False
        return self.end == other.end
    
    def __ne__(self, other):
        return self.end != other.end
    
    def __le__(self, other):
        return self.end <= other.end

    def __lt__(self, other):
        return self.end < other.end

    def __ge__(self, other):
        return self.end >= other.end

    def __gt__(self, other):
        return self.end > other.end
    
    def __str__(self):
         return "value: " +  str(self.start) + " -> " + str(self.end) + ": " + str(self.weight)    

# from dijkstras import Node
# from dijkstras import Graph
class Node:
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.color = 'white'
        self.st = None
        self.et = None
        self.parent = None
        self.string = ""
        self.dist = 9999999
        self.pred = None
        self.edgesFrom = []

    def __str__(self):
        return(str(self.name) + ": " + str(self.dist))

    def __eq__(self, other):
        if other is None:
            return None
        return self.dist == other.dist

    # def __ne__(self, other):
    #     return self.dist != other.dist

    def __le__(self, other):
        return self.dist <= other.dist

    def __lt__(self, other):
        return self.dist < other.dist

    def __ge__(self, other):
        return self.dist >= other.dist

    def __gt__(self, other):
        return self.dist > other.dist

class MinHeap:
    def __init__(self, array = None):
        self.number= 0
        if array is not None:
            self.list = self.buildHeap(array)
        else:
            self.list = []

    def __str__(self):
        print("")
        print("List: ", self.list[:self.number])
        for i in self.list[:self.number]:
            print(i.name, end=" ")
        print("\nNo. of elements: ", self.number)
        print("")
        return " "

    def heapify(self, array, index, no = None):
        if no == None:
            no = self.number
        if array == []:
            print("ERROR: Array Empty")
            return array
        elif index < 0:
            print("ERROR: Index < 0")
            return array
        else:
            if (((index + 1) * 2)) == no:
                if array[index] > array[((index + 1) * 2) - 1]:
                    array[index], array[((index + 1) * 2) - 1] = array[((index + 1) * 2) - 1], array[index]
                    array = self.heapify(array, ((index + 1) * 2) - 1, no)
                    return array
                else:
                    return array
            elif (((index + 1) * 2)) > no:
                return array
            elif (((index + 1) * 2)) < no:
                x = min(array[((index + 1) * 2) - 1], array[(index +1) * 2])
                if array[index] > x:
                    if x == array[((index + 1) * 2) - 1]:
                        array[((index + 1) * 2) - 1], array[index] = array[index], array[((index + 1) * 2) - 1]
                        array = self.heapify(array, ((index + 1) * 2) - 1, no)
                    elif x == array[((index + 1) * 2)]:
                        array[((index + 1) * 2)], array[index] = array[index], array[((index + 1) * 2)]
                        array = self.heapify(array, ((index + 1) * 2), no)
                    else:
                        pass
                return array
    
    def insert(self, node):
        print("Node name: ", node.name, "Node.dist: ", node.dist)
        self.number += 1
        self.list.append(node)

        i = self.number
        while ((i // 2) > 0) and self.list[(i // 2) - 1] > self.list[i - 1]:
            self.list[(i // 2) - 1], self.list[i - 1] = self.list[i - 1], self.list[(i // 2) - 1]
            if i // 2 == 0:
                break
            i = i // 2

    def extractMin(self):
        print("--extractMin--")
        if self.list == []:
            print("ERROR: heap empty")
            return None
        else:
            minn = self.list[0]
            self.list[0], self.list[self.number - 1] = self.list[self.number - 1], self.list[0]
            del self.list[self.number-1]
            self.number -= 1
            self.list = self.heapify(self.list, 0)
            print(minn)
            return minn
    
    def isEmpty(self):
        if self.list == []:
            print("ERROR: heap empty")
            return True
        else:
            return False
    
    def minimum(self):
        print("--minimum--")
        if self.list == []:
            print("ERROR: heap empty")
            return None
        else:
            print(self.list[0])
            return self.list[0]
    
    def buildHeap(self, array):
        self.number = len(array)
        print("--buildHeap--")
        for i in range(self.number, 1, -1):
            array = self.heapify(array, (i // 2) - 1)
        return array

    def heapSort(self, array):
        no = self.number
        while no > 1:
            if array == []:
                print("ERROR: heap empty")
                return None
            else:
                array[0], array[no - 1] = array[no - 1], array[0]
                no -= 1
                array = self.heapify(array[:no], 0, no) + array[no:]
        print("Heapsorted: ", array)
        return array

    # bubble up or trickle down based on change
    def updatePriority(self, node, newDist):
        node.dist = newDist
        index = None
        for i in range(self.number):
            if self.list[i].name == node.name:
                index = i
                break

        if index == None:
            print("ERROR: Node deos not exist")
            return

        if index // 2 == 0:
                return

        while (self.list[((index + 1) // 2) - 1] > self.list[index]):
            self.list[((index + 1) // 2) - 1], self.list[index] = self.list[index], self.list[((index + 1) // 2) - 1]
            if index // 2 == 0:
                break
            index = index // 2




                


def main():
    # tempArray = [2, 69, 3, 9, 0, 21, 4, 6]
    # print(tempArray)
    pq = MinHeap()
    # e1 = Edge(2, 3, 5)
    # e2 = Edge(3, 4, 9)
    # e3 = Edge(2, 4, 2)
    pq.insert(Node(1))
    pq.insert(Node(2))
    pq.insert(Node(4))
    print(pq)
    pq.extractMin()
    print(pq)
    pq.minimum()
    print(pq)
    pq.heapSort(pq.list)


if __name__ == '__main__':
    main()

