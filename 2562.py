cur_max = 0
for i in range(1,9+1):
    a = int(input())
    if a > cur_max:
        cur_max = a
        memo = i
print(cur_max)
print(memo)