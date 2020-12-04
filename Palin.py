s = raw_input("Enter the word:")
def isPalindrome(s):
	rev = ''.join(reversed(s))
	if (s == rev):
		print "Palindrome",s,"and",rev
	else:
		print "Not Palindrome", s, "and",rev

isPalindrome(s)