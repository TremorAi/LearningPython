# min = 1
# max = 100000
# sum = 0
# half = 0

# challenge 1 solved easy way
# for n in range(min, max+1):
#     sum+=n

# print(str(sum))

#better method
# 1 2 3 4 5 6 7 8 9 10
# 1 2    +        9 10 = 11
# half = max / 2
# sum = half * max + half
# print(int(sum * 5))


# 
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

lenthing = len(word1)

for n in range(lenthing):
    teststring = word1.replace(word1[n], "")
    if teststring == word2:
        print(f"{teststring} you did it!")
        
    else:
        print(f"{teststring} failed")
        
 

    

