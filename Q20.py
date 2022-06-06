primes = []
for i in range(2, 1001):
    flag = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = False
    if flag:
        primes.append(i)


def check_prime(numb: int):
    for i in primes:
        if numb % i == 0:
            return False
    return True


def check(numb: int):
    array = list(str(numb))
    permutations = []
    flag = True
    for _ in range(0, len(array)):
        last_digit = array.pop()
        array = [last_digit]+array
        new_arr = array.copy()
        value = int(''.join(new_arr))
        if not check_prime(value):
            flag = False
            break
    return flag


all_cases = []
digits = [1, 3, 7, 9]
# FOR 4 DIGITS
# for d1 in digits:
#     for d2 in digits:
#         for d3 in digits:
#             for d4 in digits:
#                 numb = d1*1+d2*10+d3*100+d4*1000
#                 if check(numb):
#                     print(numb)
# FOR 5 DIGITS
# for d1 in digits:
#     for d2 in digits:
#         for d3 in digits:
#             for d4 in digits:
#                 for d5 in digits:
#                     numb = d1*1+d2*10+d3*100+d4*1000+d5*10000
#                     if check(numb):
#                         print(numb)
