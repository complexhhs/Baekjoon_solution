import sys
case = int(input())

for _ in range(case):
	a,b = map(int,sys.stdin.readline().split())
	print(a+b)