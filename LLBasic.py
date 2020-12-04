class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__():
		return self.data

class LinkedList:

	def __init__(self):
		self.head = None

	def __repr__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next

		nodes.append("None")
		return "->" .join(nodes)
	"""Traverse Linked list
	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next
	"""

	#Insert Node at the beginning of linked list
	def add_first(self, node):
		node.next = self.head
		self.head = node

	#Insert node at the end of linked list
	def add_last(self, node):

		if not self.head:
			self.head = node
			return
		for current_node in self:
			pass
		current_node.next = node


	def add_after(self, target_node_data, new_node):
		if not self.head:
			raise Exception("List is Empty")

		for node in self:
			if node.data == target_node_data:
				new_node.next = node.next
				node.next = new_node
				return
		raise Exception("Node with data '%s' not found" % target_node_data)


llist = LinkedList()
#print llist
first_node = Node("a")
llist.head = first_node
second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
llist.add_first(Node("d"))
llist.add_last(Node("e"))
llist.add_after("a", Node("g"))
print llist
