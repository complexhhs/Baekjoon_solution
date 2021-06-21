def quadrant(x,y):
	if x>0 and y>0:
		ans = 1
	elif x<0 and y>0:
		ans = 2
	elif x>0 and y<0:
		ans = 4
	else:
		ans = 3
	return ans
	
x = float(input())
y = float(input())

answer = quadrant(x,y)
print(answer)