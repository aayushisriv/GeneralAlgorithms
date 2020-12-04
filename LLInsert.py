class Node:#Node class
	
	#Function to initialize node object
	def __init__(self,data):
		self.data = data #assign data
		self.next = None # initialize next as null

#Linked List class
class LinkedList:

	#function to initialize linked list object
	def __init__(self):
		self.head = None

	#function to insert node at the beginning
	def push(self, new_data):

		#allocate the node and put into data
		new_node =  Node(new_data)

		#make next of new node as head
		new_node.next = self.head

		#move the head to point to point to new node
		self.head = new_node

	def insertAfter(self, prev_node, new_data):

		#check if the given prev node exists
		if prev_node is None:
			print "The given previous node must inLinkedList"
			return

		#create new node and put in the data
		new_node = Node(new_data)

		#make next of new Node as next of prev_node
		new_node.next = prev_node.next

		#make next of prev_node as new_node
		prev_node.next = new_node


	#Appends a new node at the end
	def append(self, new_data):

		#create a new node, put in the data, set next as None
		new_node = Node(new_data)

		#if linked list is empty, then make the new node as head
		if self.head is None:
			self.head = new_node
			return

		#else traverse the last node
		last = self.head
		while(last.next):
			last = last.next

		#change the next of last node
		last.next = new_node

	#utility function to print the linked list
	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next


#Code Execution starts here
if __name__ == '__main__':

	#start with the empty list
	llist = LinkedList()

	#insert 6. so linked list becomes 6->None
	llist.append(6)

	#insert 7 at the beginning.so linked list becomes 7->6->None
	llist.push(7)

	#insert 1 at the beginning. 1->7->6->None
	llist.push(1)

	 #insert 4 at the end.1->7->6->4->None
	llist.append(4)

	#insert 8 after 7. 1->7->8->6->4->None
	llist.insertAfter(llist.head.next,8)

	print "Created linked list is: "
	llist.printList()

