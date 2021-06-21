num = int(input())
cnt = 0
while True:
    cnt += 1
    if 3*cnt*(cnt-1)+1 >= num:
        break
print(cnt)