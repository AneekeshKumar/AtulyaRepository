def doubling(a):
    k = 0
    while k < len(a):
        print(2 * a[k], end='')
        k += 1


x = input("Enter the string: ")
doubling(x)
