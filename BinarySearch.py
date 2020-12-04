def binarysearch(array, target):
	lower = 0
	upper = len(array)
	while (lower < upper):
		x = lower + (upper - lower) // 2
		val = array[x]
		if target == val:
			return x
		elif target > val:
			if lower == x:
				break
			lower = x
		elif target < val:
			upper = x
l = [1,2,4, 5,19,24]
binary_search(l,5)