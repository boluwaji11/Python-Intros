import random

def main():
    num1 = random_values()
    num2 = random_values()
    #print(num1, num2)
    #display_problem(num1, num2)
    #display_answer(num1, num2)
    bolu(num1,num2)
    ayo(num1,num2)
    
def random_values():
    for numbers in range(2):
        numbers = random.randint(0,999)
        #print(numbers)
        return numbers
def bolu(num1, num2):
    result = num1 * num2
    print(num1)
    print(num2)
    print(result)

def ayo(num1,num2):
    result = num1 + num2
    print(result)

main()
