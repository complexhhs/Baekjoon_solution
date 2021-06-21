num_len, x = map(int,input().split())

a = [int(i) for i in input().split()]
string = ''
for i in range(num_len):
	if x > a[i]:
		string += str(a[i])+' '
print(string)