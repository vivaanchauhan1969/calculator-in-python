#adding
def add (n1 ,n2):
    n1 + n2

#subtracting
def subtracting (n1 , n2):
    return n1 - n2

#Multplying 
def multplying (n1 , n2):
    return n1 * n2

def divison (n1 , n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtracting,
    "*": multplying,
    "/":divison
}

num1 = int (input ("what is the first number?: "))
num2 = int (input("what is the second number? "))

for symbol in operation:
    print(symbol)

operation_symbol = input('pick a operation from the above: ')
if operation_symbol == "+":
    answer = num1 + num2
elif operation_symbol == "-":
    answer = num1 - num2
elif operation_symbol == "*":
    answer = num1 * num2
elif operation_symbol == "/":
    answer = num1 / num2
print(f'{num1} {operation_symbol} {num2} = {answer}')
Go_agian = True

while Go_agian == True:
    x =input ('if you want to go agian then type "y" and if you are not going agian the type "n" ') 
    if x == "y" :
        Go_agian = True
    elif x == "n":
        Go_agian = False
        exit()
    calculation_function = operation[operation_symbol]
    for symbol in operation:
        print(symbol)
    operation_symbol = input("pick another operation: ")
    num3 = int (input('pick another number?: '))
    al = answer
    if operation_symbol == "+":
        answer = al + num3
    elif operation_symbol == "-":
        answer = al - num3
    elif operation_symbol == "*":
        answer = al * num3
    elif operation_symbol == "/":
        answer = al / num3
    print(f'{al} {operation_symbol} {num3} = {answer}')
