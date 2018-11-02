__author__ = "tremor"


def main():
    number1 = input("Input the first number: ")
    number2 = input("Input the second number: ")
    operation = input("Input a operation(+, -, *, **, /): ")

    calc(number1,number2,operation)

def calc(number1,number2,operation):
    number1 = int(number1)
    number2= int(number2)

    if dict1.get(operation):
        dict1[operation](number1,number2)



def add(number1, number2):
    print(number1 + number2)

def minus(number1, number2):
    print(number1 - number2)

def multiply(number1, number2):
    print(number1 * number2)

def power(number1, number2):
    print(number1 ** number2)

def divide(number1, number2):
    print(number1 / number2)

#pow(number1, number2)


dict1 = {"+":add,"-":minus,"*":multiply,"**":power,"/":divide}

if __name__ == '__main__':
    main()


	

