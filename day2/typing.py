__author__ = "Tremor"

import os
 
def main():
	string1 = input("What is the first string: ")
	string2 = input("What is the second string: ")
	addstrings(string1,string2)

def addstrings(string1, string2):
	print("{} {}".format(string1,string2))

if __name__ == '__main__':
	main()



