class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        print("before heapify",self.heap)
        self._heapify_up()
        print("after heapify",self.heap)

    def _heapify_up(self, index=None):
        if index is None:
            index = len(self.heap) - 1

        while index > 0:
            print("index in _heapify_up is:",index)
            parent_index = (index - 1) // 2
            print("parent_index is",parent_index)
            if self.heap[index] > self.heap[parent_index]:
                # Swap with parent if the current element is greater
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                print("Inside the heap",self.heap)
                index = parent_index
            else:
                break

    def delete_at_index(self, index):
        # Max Heap: [10, 8, 3, 1, 5]
        # Index is 1
        if index < 0 or index >= len(self.heap):
            return None
        
        deleted_value = self.heap[index]
        self.heap[index] = float('inf')  # Set to positive infinity for deletion
        print("heap after assigning the infinity value to the deleted value",self.heap)
        self._heapify_up(index)
        self.delete_max()
        return deleted_value
    
    def delete_max(self):
        if len(self.heap) == 0:
            return None
            
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        popped_element=self.heap.pop()
        print("popped_element is",popped_element)
        self.heap[0] = popped_element
        print("heap after assigning the popped value to the zero index",self.heap)
        self._heapify_down()
        return max_value

    def _heapify_down(self, index=0):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            print("left_child_index",left_child_index)
            print("right_child_index",right_child_index)
            print("largest",largest)
            
            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            print("Max value index in heapify is",largest)
            if largest != index:
                # Swap with the larger child if needed
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
                print("heap after finding the max index and assinging the value",self.heap)
                print("index after assinging the max",index)
            else:
                break

# Example Usage:
heap = MaxHeap()
heap.insert(5)
heap.insert(8)
heap.insert(3)
heap.insert(1)
heap.insert(10)

print("Max Heap:", heap.heap)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# deleted_value = heap.delete_at_index(2)
# print("Deleted Value at index 2:", deleted_value)
# print("Max Heap after deletion at index 2:", heap.heap)

deleted_value = heap.delete_at_index(1)
print("Deleted Value at index 1:", deleted_value)
print("Max Heap after deletion at index 1:", heap.heap)


