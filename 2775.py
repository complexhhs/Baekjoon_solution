case = int(input())

def check_people(h,w):
	aux=[1 for i in range(w)]
	for ih in range(h+1):
		for iw in range(w):
			if iw == 0:
				aux[iw]=1
			else:
				aux[iw] = aux[iw-1]+aux[iw]
	return aux[iw]

ans=[]

for i in range(case):
	h = int(input())
	w = int(input())
	ans.append(check_people(h,w))

for i in range(case):
	print(ans[i])