def operation(a, b, c):
    if b == "+":
        print(a + c)
    elif b == "/":
        print(a / c)
    elif b == "*":
        print(a * c)
    elif b == "-":
        print(a - c)
    else:
        print("invalid operator")


first = input("enter the first digit: ")
op = input("enter the operator: ")
second = input("enter the second digit: ")
operation(int(first), op, int(second))
