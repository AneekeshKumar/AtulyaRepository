import random

n = []
len = int(input("enter the length of array: "))
for i in range(0, len):
    n.append(random.randint(1, 99))

print(n)
count = 0
max = 0
value = 0
for i in range(0, len):
    for j in range(0, len):
        if (n[i] == n[j]):
            count += 1
    if (count > max):
        max = count
        value = n[i]
    count = 0
print(value, "repeated", max, "times")
