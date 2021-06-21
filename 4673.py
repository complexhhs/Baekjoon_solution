def selfnum(a):
	digits = [int(str(a)[i]) for i in range(len(str(a)))]
	res = a+sum(digits)
	return res

black_list = []
for i in range(10000):
    if i in black_list:
        pass
    else:
	    res = selfnum(i)
	    while res <= 10000:
		    if res in black_list:
		    	break
		    else:
		    	black_list.append(res)
		    	res = selfnum(res)
	
for i in range(10000):
	if i in black_list:
		pass
	else:
		print(i)