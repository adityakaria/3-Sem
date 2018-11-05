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
        print("No. of elements: ", self.number)
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
    
    def insert(self, value):
        print("--insert--  value:", value)
        self.number += 1
        self.list.append(value)

        i = self.number
        while ((i // 2) > 0) and self.list[(i // 2) - 1] > self.list[i - 1]:
            self.list[(i // 2) - 1], self.list[i - 1] = self.list[i - 1], self.list[(i // 2) - 1]
            if i // 2 == 0:
                break
            i = i // 2

    def extractMin(self):
        print("--extractMax--")
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
                


def main():
    tempArray = [2, 69, 3, 9, 0, 21, 4, 6]
    print(tempArray)
    pq = MinHeap(tempArray)
    pq.insert(90)
    print(pq)
    pq.extractMin()
    print(pq)
    pq.minimum()
    print(pq)
    pq.heapSort(pq.list)


if __name__ == '__main__':
    main()

