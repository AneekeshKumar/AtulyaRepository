def order(x, y):
    if y == "asc.":
        x.sort()
    elif y == "desc.":
        x.sort(reverse=True)
    elif y == "none.":
        return x
    return x


list2 = [12, 243, 2531, 5213, 32, 23, 12, 475, 87, 264, 927]
v = order(list2, "desc.")
print(v)
