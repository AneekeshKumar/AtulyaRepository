list = [10, 13, 10, 45, 10, 56]
i = 0
while i < len(list):
    j = 0
    while j < i:
        if list[i] == list[j]:
            a = list[i]
        j += 1
    i += 1
print("the number is: " + str(a))
