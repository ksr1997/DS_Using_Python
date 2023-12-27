# Python3 program to check whether a 
# given array represents a max-heap or not 

# Returns true if arr[i..n-1] 
# represents a max-heap 
def isHeap(arr, i, n): 
	
	# If (2 * i) + 1 >= n, then leaf node, so return true 
	if i >= int((n - 1) / 2):
		print("recurssion breaking condition i is",i)
		print("recurssion breaking condition int((n-1)/2) is",int((n-1)/2)) 
		return True
	
	print("root is",arr[i])
	print("root index is",i)
	print("left child is",arr[2*i+1])
	print("right child is",arr[2*i+2])
	print("left child index is",2*i+1)
	print("right child index is",2*i+2)
	if(arr[i] >= arr[2 * i + 1] and arr[i] >= arr[2 * i + 2] and
      isHeap(arr, 2 * i + 1, n) and isHeap(arr, 2 * i + 2, n)):
		return True
	return False

# Driver Code 
if __name__ == '__main__': 
	arr = [90, 15, 10, 7, 12, 2, 7, 3]
	n = len(arr) - 1
	'''
	          90
		 15        10
       7   12    2    7
	3
	'''
	print("arr is",arr)
	print("n is ",n)
	if isHeap(arr, 0, n): 
		print("Yes") 
	else: 
		print("No") 

# This code is contributed by PranchalK 
