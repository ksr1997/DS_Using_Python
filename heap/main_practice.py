

class MaxHeap: 
	arr = [] 
	maxSize = 0
	heapSize = 0
	
    
	def __init__(self, maxSize): 
		self.maxSize = maxSize 
		self.arr = [None]*maxSize 
		self.heapSize = 0

	def getMax(self): 
		return self.arr[0] 

	def curSize(self): 
		return self.heapSize
	
	def parent(self, i): 
		return (i - 1) // 2
	
	def insertKey(self, x): 
		if self.heapSize == self.maxSize: 
			print("\nOverflow: Could not insertKey\n") 
			return
		
		self.heapSize += 1
		i = self.heapSize - 1
		self.arr[i] = x
		
		while i != 0 and self.arr[self.parent(i)] < self.arr[i]: 
			temp = self.arr[i] 
			self.arr[i] = self.arr[self.parent(i)] 
			self.arr[self.parent(i)] = temp 
			i = self.parent(i)
		print(self.arr)
	
	def lChild(self, i): 
		return (2 * i + 1) 

	# Returns the index of the right child. 
	def rChild(self, i): 
		return (2 * i + 2) 
		
	def MaxHeapify(self, i): 
		l = self.lChild(i) 
		r = self.rChild(i) 
		largest = i 
		if l < self.heapSize and self.arr[l] > self.arr[i]: 
			largest = l 
		if r < self.heapSize and self.arr[r] > self.arr[largest]: 
			largest = r 
		if largest != i: 
			temp = self.arr[i] 
			self.arr[i] = self.arr[largest] 
			self.arr[largest] = temp 
			self.MaxHeapify(largest) 	
			
	def deleteKey(self, i): 
		self.increaseKey(i, float("inf")) 
		return self.removeMax()

	def increaseKey(self, i, newVal): 
		self.arr[i] = newVal 
		while i != 0 and self.arr[self.parent(i)] < self.arr[i]: 
			temp = self.arr[i] 
			self.arr[i] = self.arr[self.parent(i)] 
			self.arr[self.parent(i)] = temp 
			i = self.parent(i)
			print("i is ",i)
		print(self.arr)
		
	def removeMax(self): 
		if self.heapSize <= 0: 
			return None
		if self.heapSize == 1: 
			self.heapSize -= 1
			return self.arr[0] 
		root = self.arr[0] 
		self.arr[0] = self.arr[self.heapSize - 1] 
		self.heapSize -= 1
		self.MaxHeapify(0) 
		return root       


    
if __name__ == '__main__': 
	h = MaxHeap(15)
	print("arr is", h.arr)
	print("maxSize is",h.maxSize)
	print("heapSize is",h.heapSize)
	h.insertKey(3) 
	h.insertKey(10) 
	h.insertKey(12) 
	h.insertKey(8) 
	h.insertKey(2) 
	h.insertKey(14)
    
	print("The current size of the heap is "+ str(h.curSize()) + "\n") 
	print("The current maximum element is " + str(h.getMax()) + "\n")
	print("Arr before deletion",h.arr)
	deleted_value=h.deleteKey(2)
	print("deleted_value is",deleted_value)
	print("The current size of the heap is "+ str(h.curSize()) + "\n") 
	print("Arr after deletion",h.arr)