a=int(input())
b=int(input())
c=int(input())
res = a*b*c
res_list = [int(str(res)[i]) for i in range(len(str(res)))]
cnt0 = 0
cnt1 = 0
cnt2 = 0 
cnt3 = 0 
cnt4 = 0 
cnt5 = 0
cnt6 = 0 
cnt7 = 0
cnt8 = 0
cnt9 = 0
for i in res_list:
    if i == 0:
        cnt0 += 1
    elif i == 1:
        cnt1 += 1
    elif i == 2:
        cnt2 += 1
    elif i == 3:
        cnt3 += 1
    elif i == 4:
        cnt4 += 1
    elif i ==5 :
        cnt5 +=1
    elif i==6:
        cnt6 += 1
    elif i==7:
        cnt7 += 1
    elif i==8:
        cnt8 += 1
    else:
        cnt9 += 1
print(cnt0)
print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)
print(cnt5)
print(cnt6)
print(cnt7)
print(cnt8)
print(cnt9)