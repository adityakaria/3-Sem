class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def heapifyUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] > self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.heapifyUp(self.currentSize)

    def heapifyDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.maxChild(i)
          if self.heapList[i] < self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def maxChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] > self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def extractMax(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.heapifyDown(1)
      return retval
    
    def show(self):
      print(self.heapList)

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.heapifyDown(i)
          i = i - 1


def main():
    bh = BinHeap()
    ch=0
    while(ch!=6):
        print(" 1).Insert new Element\n 2).Extract-max\n 3).show Max Element\n 4).BuildHeap \n 5).HeapSort \n 9).Quit program \n")
        ch=int(input("Enter choice :"))
        if ch==1:
            temp=0
            while True:
              temp=input("Enter Element : ")
              if temp == 'k':
                break
              bh.insert(int(temp))

        elif ch==2:
            print("Max was : " , bh.extractMax())
        
        elif ch==3:
            print("Max is : " , bh.heapList[1])
        
        elif ch==4:
             bh.buildHeap([3, 5, 0, 9])
        
        elif ch==5:
            result=[]
            for i in range(0,bh.currentSize):
                result.append(bh.extractMax())
            bh.buildHeap(result)
            print(result)

        
    
if __name__=='__main__':
    main()
