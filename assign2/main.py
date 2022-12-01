
def sum(number,number2):
    return print(number + number2)
    
def sub(number,number2):
    return print(number - number2)

def mul(number,number2):
    return print(number * number2)

def div(number, number2):
    return print(number / number2)


while True:
    number = int(input("choose a number:"))
    number2 = int(input("choose another one:"))
    operator = input("Options are: +, -, * or /. \n Write 'exit' to finish.")
    if operator == "+":
        sum(number,number2)
        
    elif operator == "-":
        sub(number,number2)

    elif operator == "*":
        mul(number,number2)

    elif operator == "/":
        div(number,number2)

    elif operator == "exit":
        break

