
def search(arr,x):
	for i in range(len(arr)):

		if arr[i] == x:
			#return i
			print "Found",x
		else:
		print "Not present in list"
l = [1,2,3,5,6,7,8]
search(l,7)