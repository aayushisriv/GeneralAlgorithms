
import copy

class Palindrome:

	def __init__(self,string):
		self.string = string

	def isPal(self,string, l, h):
		while l < h:
			if string[l] != string[h]:
				return False
			l += 1
			h -= 1
		return True


	def PalPartition(self, allP, presP, begin, end, string):
		
		if begin >= end:
			ab = copy.deepcopy(presP)
			allP.append(ab)

			return
		for i in range(begin,end):

			if self.isPal(string, begin, i):

				presP.append(string[begin:i + 1])

				self.PalPartition(allP, presP, i+1, end, string)

				presP.pop()



	def PrintPart(self,string):

		m = len(string)
		allP = []
		presP = []

		self.PalPartition(allP, presP, 0, m, string)

		for i in range(len(allP)):

			for j in range(len(allP[i])):
				print (allP[i][j],end =" ")

			print ("\n")
		print()

val = input("Enter the string: ")
val = val.upper()
vs =  Palindrome(val)
vs.PrintPart(val)








