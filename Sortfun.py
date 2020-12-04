data_list = []
n = int(raw_input("Enter number of elements:"))
for i in range(0,n):
	ele = int(raw_input())
	data_list.append(ele)
print "Initial list:",data_list
new_list = []

while data_list:
	minm = data_list[0]
	for x in data_list:
		if x > minm:
			minm = x
	new_list.append(minm)
	data_list.remove(minm)

print "Desc sorted list:",new_list