import math

def cal_count(a,b):
	dist = abs(b-a)
	return math.ceil(math.sqrt(dist*4)-1)

num = int(input())
ans = []
for i in range(num):
	a,b = map(int,input().split())
	ans.append(cal_count(a,b))

for i in range(num):
	print(ans[i])