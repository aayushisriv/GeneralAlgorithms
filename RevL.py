lst = []
n = int(raw_input("Enter number of elements:"))
for i in range(0,n):
	ele = int(raw_input())
	lst.append(ele)

print "Initial List:",lst

def rev(l):
	return l[::-1]
rev(lst)
print "Reversed List:", rev(lst)