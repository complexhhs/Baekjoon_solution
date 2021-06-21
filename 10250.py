case = int(input())
ans = []

def check_room(h,w,n):
	cnt_w = 1
	cnt_h = 0
	while True:
		cnt_h += 1
		if cnt_h > h:
			cnt_h = 1
			cnt_w += 1
		if (cnt_w-1)*h+cnt_h == n:
			break
	if cnt_w//10 == 0:
		return str(cnt_h)+'0'+str(cnt_w)
	else:
		return str(cnt_h)+str(cnt_w)

for i in range(case):
	h,w,n = map(int,input().split())
	ans.append(check_room(h,w,n))

for i in range(case):
	print(ans[i])