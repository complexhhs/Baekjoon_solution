import sys

# check = True
ans = []
for line in sys.stdin:
	a,b = map(int,line.strip().split())
	ans.append(a+b)
# while check:
	# a,b = map(int,sys.stdin.strip().split())
	# ans.append(a+b)

for i in ans:	
	print(i)