def prime_number_division(number):
    if number == 1:
        return

    for i in range(2,number+1):
        if number % i == 0:
            while number % i == 0:
                print(i)
                number /= i

number = int(input())
prime_number_division(number)
