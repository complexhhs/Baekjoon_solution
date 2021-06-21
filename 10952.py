check = True
ans = []
while check:
	a,b = map(int,input().split())
	if a == 0 and b==0:
		break
	ans.append(a+b)

for i in ans:	
	print(i)