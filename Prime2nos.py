a = int(raw_input("Enter first no."))
b = int(raw_input("Enter second no."))
for x in range (a, b):
	if all (x % i != 0 for i in range(2,x)):
		print x