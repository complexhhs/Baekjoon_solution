import sys
sys.setrecursionlimit(10000)

def delivery(k):
	if k in memo:
		return memo[k]
	
	if k<0 or k == 1 or k == 2:
		return 5000
	elif k == 3:
		memo[k] = 1
		return memo[k]
	elif k == 5: 
		memo[k] = 1
		return memo[k]
	else:
		memo[k] = min(delivery(k-3), delivery(k-5))+1
		return memo[k]
		
num = int(input())
memo = {}
a = delivery(num)
if a == 5000 or a == 5001:
	print(-1)
else:
	print(a)