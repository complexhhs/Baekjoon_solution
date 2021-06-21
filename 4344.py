import sys
num_case = int(input())
for _ in range(num_case):
    score_list = [float(i) for i in sys.stdin.readline().split()]
    num_student = int(score_list[0])
    score_list = score_list[1:]
    mean = sum(score_list)/num_student
    cnt = 0
    for i in range(num_student):
        if score_list[i] > mean:
            cnt += 1
    print('%3.3f'%(float(cnt)/float(num_student)*100)+'%')        