
# A Python program to demonstrate common binary heap operations
  
# Import the heap functions from python library
from heapq import heappush, heappop, heapify 
  
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

# Insert - O(logn)
# extraxt_min - O(logn)
# decreaseKey - O(logn)
# Makequee - O(nlogn)

# A class for Min Heap
class MinHeap:
      
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
  
    def parent(self, i):
        return i//2
    
    def children(self, i):
        return [2*i, 2*i + 1]
      
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)           
  
    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
              
    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)
  
    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()
  
    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]
    def makeQueue(self, arr):
        for i in arr:
            self.insertKey(i)
        return self.heap
            

# Driver pgoratm to test above function
# heapObj = MinHeap()
# print(heapObj.heap)
# heapObj.insertKey(3)
# print(heapObj.heap)
# heapObj.insertKey(2)
# print(heapObj.heap)
# heapObj.deleteKey(1)
# print(heapObj.heap)
# heapObj.insertKey(15)
# print(heapObj.heap)
# heapObj.insertKey(5)
# print(heapObj.heap)
# heapObj.insertKey(4)
# print(heapObj.heap)
# heapObj.insertKey(45)
# print(heapObj.heap)

# print(heapObj.extractMin())
# print(heapObj.getMin())
# heapObj.decreaseKey(2, 1)
# print(heapObj.getMin())
# print(heapObj.children(3))

# heapObj = MinHeap()
# print(heapObj.makeQueue([5, 15, 4, 45, 3]))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
