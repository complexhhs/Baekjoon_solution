n = int(input())
ans = []

for idx,_ in enumerate(range(n)):
	a,b = map(int,input().split())
	print('Case #{:d}: {:d}'.format(idx+1,a+b))