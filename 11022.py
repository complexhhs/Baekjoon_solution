n = int(input())
for idx, _ in enumerate(range(n)):
	a,b = map(int, input().split())
	print('Case #{:d}: {:d} + {:d} = {:d}'.format(idx+1,a,b,a+b))