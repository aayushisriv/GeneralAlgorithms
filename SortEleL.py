lst = []
n = int(raw_input("Enter number of elements:"))
for i in range(0,n):
	ele = int(raw_input())
	lst.append(ele)
print "Original list:",lst
lst.sort(reverse=True)
print "Sorted List:",lst