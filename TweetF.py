from collections import Counter
#import sys


tweet_names = []
n = int(input("Enter number of tweets: "))
for i in range(0,n):
	ele = input()
	tweet_names.append(ele)
print("Tweet List is: ")
print(tweet_names)


uniq_names = [pref_names.split()[0] for pref_names in tweet_names]
#print (uniq_names) #names of user

times = Counter(uniq_names)
#print(times)
repeat = times.values()
#print(repeat)

for element in set(repeat):
	dup1 = ([(key,value) for key,value in sorted(times.items()) if value == element])

	if len(dup1) > 1:
		for (key, value) in dup1:
			print(key,'',value)
	max_value = max(times.values())
	temp_max_result = [(key,value) for key,value in sorted(times.items()) if value == max_value]

	if temp_max_result != dup1:
		for (key,value) in temp_max_result:
			print ("The user with maximum number of tweets is:")
			print(key,'',value)	
			#sys.exit()