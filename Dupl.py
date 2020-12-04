lst = []
n = int(raw_input("Enter number of elements:"))
for i in range(0,n):
	ele = int(raw_input())
	lst.append(ele)
print "Initial List:",lst
print "Set of duplicates:", set([x for x in lst if lst.count(x) > 1])