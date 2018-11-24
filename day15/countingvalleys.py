__author__ = "TremorAi"

def countingvalleys(s):
    elevation = 0
    in_valley = False
    valleys = 0
    for i in s:
        if i == "D":
            elevation -= 1
        elif i == "U":
            elevation += 1

        if i == "D" and elevation == -1:
            in_valley = True
            valleys += 1
    print(valleys)
         

countingvalleys("DDUUDDUUDDUUDDUU")
