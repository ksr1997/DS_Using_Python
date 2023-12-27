# Python3 code To check if a binary
# tree is a MAX Heap or not


class GFG:
	def __init__(self, value):
		self.key = value
		self.left = None
		self.right = None

	def count_nodes(self, root):
		if root is None:
			return 0
		else:
			return (1 + self.count_nodes(root.left) +
					self.count_nodes(root.right))

	def heap_property_util(self, root):

		if (root.left is None and
				root.right is None):
			return True

		if root.right is None:
			return root.key >= root.left.key
		else:
			if (root.key >= root.left.key and
					root.key >= root.right.key):
				return (self.heap_property_util(root.left) and
						self.heap_property_util(root.right))
			else:
				return False

	def complete_tree_util(self, root,
						index, node_count):
		if root is None:
			return True
		if index >= node_count:
			return False
		return (self.complete_tree_util(root.left, 2 *
										index + 1, node_count) and
				self.complete_tree_util(root.right, 2 *
										index + 2, node_count))

	def check_if_heap(self):
		node_count = self.count_nodes(self)
		if (self.complete_tree_util(self, 0, node_count) and
				self.heap_property_util(self)):
			return True
		else:
			return False


# Driver's Code
if __name__ == '__main__':
	root = GFG(5)
	root.left = GFG(2)
	root.right = GFG(3)
	root.left.left = GFG(1)

	# Function call
	if root.check_if_heap():
		print("Given binary tree is a heap")
	else:
		print("Given binary tree is not a Heap")

# This code has been
# contributed by Yash Agrawal