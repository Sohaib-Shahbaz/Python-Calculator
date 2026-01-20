from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    accumulate = True
    n1 = float(input("Enter first number: "))

    while accumulate == True:
        sum = input("Would you like to add, subtract, multiply, or divide? '+' '-' '*' '/' : ")
        n2 = float(input("Enter second number: "))
        print(f"{n1} {sum} {n2} = {(operations[sum](n1,n2))}")
        result = (operations[sum](n1,n2))
        con = input(f"Would you like to continue calculating with {result}? 'y' or 'n': ")
        if con == 'y':
            n1 = result
            print(result)
        elif con == 'n':
            accumulate = False
            print("\n" * 25)
            print(logo)
            calculator()
        else:
            print("That is not a valid input. Try again.")
            con = input(f"Would you like to continue calculating with {result}? 'y' or 'n': ")
            print(result)


calculator()