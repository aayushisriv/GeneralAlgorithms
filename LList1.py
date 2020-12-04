class Node:

	#Function to initialise the node object
	def __init__(self, data):
		self.data = data #Assign data
		self.next = None #initialise next as null


	#Linked list class contains a Node object
class LinkedList:

	#Function to initialise head
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while (temp):
			print temp.data
			temp = temp.next



	#Code execution starts here
if __name__ == '__main__':

	#Start with the empty list
	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)

	llist.head.next = second #link first node with second
	second.next = third #link second node with third

	llist.printList()
