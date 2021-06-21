a = int(input())
b = input()

digit_1 = a*int(b[2])
digit_2 = a*int(b[1])
digit_3 = a*int(b[0])

print(digit_1)
print(digit_2)
print(digit_3)
print(100*digit_3+10*digit_2+digit_1)