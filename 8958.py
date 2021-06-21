num = int(input())
str_buff = []
for i in range(num):
	str_buff.append(str(input()))

for i in range(num):
	cnt = 0 
	total_score = 0
	for ii in range(len(str_buff[i])):
		if ii == 0 and str_buff[i][ii]=='O':
			cnt = 1
			total_score += cnt
		elif ii == 0 and str_buff[i][ii] == 'X': 
			cnt = 0
			total_score += cnt
		elif ii != 0: 
			if str_buff[i][ii] == 'O' and str_buff[i][ii] == str_buff[i][ii-1]:
				cnt += 1
				total_score += cnt
			elif str_buff[i][ii] == 'O' and str_buff[i][ii] != str_buff[i][ii-1]:
				cnt = 1
				total_score += cnt
	print(total_score)