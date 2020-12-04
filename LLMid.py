def findMid(head):
	curr = head
	count = 0
	while curr.next is not None:
		count += 1
		curr = curr.next

	if (count % 2 == 0):
		n = (count // 2)
		curr =  head
		while n > 0:
			curr = curr.next
			n = n - 1
		return curr

	else:
		n = (count // 2) + 1
		curr = head
		while n > 0:
			curr = curr.next
			n = n - 1
		return curr
		