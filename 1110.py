a=int(input())
cnt = 1 
two_digit = [0 for i in range(2)]

if a < 10:
    two_digit[0]=0
    two_digit[1]=a
else:
    two_digit[0]=str(a)[0]
    two_digit[1]=str(a)[1]
new_sum=int(two_digit[0])+int(two_digit[1])
if new_sum >= 10:
    new_num=int(str(two_digit[1])+str(new_sum)[1])
else:
    new_num=int(str(two_digit[1])+str(new_sum)) 

while new_num != a:
    cnt += 1
    if new_num < 10:
        two_digit[0]=0
        two_digit[1]=new_num
    else:
        two_digit[0]=str(new_num)[0]
        two_digit[1]=str(new_num)[1]
    new_sum=int(two_digit[0])+int(two_digit[1])
    if new_sum >= 10:
        new_num=int(str(two_digit[1])+str(new_sum)[1])
    else:
        new_num=int(str(two_digit[1])+str(new_sum)) 

print(cnt)