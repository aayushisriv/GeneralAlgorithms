from collections import defaultdict
def getFrequencyMap(arr,n):
	hashMap = defaultdict(lambda:0)
	for i in range(n):
		hashMap[arr[i]] += 1
	return hashMap

def hasDigit(hashMap, digit):
	if hashMap[digit] > 0:
		hashMap[digit] -= 1
		return True

	return False

def getMaxTime_value(arr, n):
	hashMap = getFrequencyMap(arr, n)
	flag = False
	time_value = ""

	for i in range(2,-1,-1):
		if hasDigit(hashMap,i) == True:
			flag = True
			time_value += str(i)
			break

	if not flag:
		return "-1"

	flag = False
	