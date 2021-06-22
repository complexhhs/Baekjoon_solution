def prime_number_division(number):
    if number == 1:
        return 0

    for i in range(2,number):
        if number % i == 0:
            return 0
    return 1

condition = True
while condition:
    number = int(input())
    if number == 0:
        break
    cnt = 0
    for i in range(number, 2*number+1):
        cnt += prime_number_division(i)
    print(cnt)
