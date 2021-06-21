num = int(input())
cnt = 0
while True:
    cnt += 1
    if cnt*(cnt+1)/2 >= num:
        break
l_cnt = num-cnt*(cnt-1)/2
if cnt%2 == 1:
    print(str(int(cnt+1-l_cnt))+'/'+str(int(l_cnt)))
else:
    print(str(int(l_cnt))+'/'+str(int(cnt+1-l_cnt)))