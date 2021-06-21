def check_han(a):
	digits = [int(str(a)[i]) for i in range(len(str(a)))]
	if len(digits) == 1 or len(digits) == 2:
		return 1
	else:
		st = digits[0]-digits[1]
		for i in range(1,len(digits)-1):
			if digits[i]-digits[i+1] != st:
				a = 1
				break
			else:
				a =0 
		if a==1:
			return 0
		else: 
			return 1

a=int(input())
cnt = 0
for i in range(a):
	cnt+=check_han(i+1)
print(cnt)		