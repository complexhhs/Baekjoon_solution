num_len = int(input())
score = [float(i) for i in input().split()]
dum = max(score)
total_sum = 0
for i in range(num_len):
    if score[i] < dum:
        score[i] = score[i]/dum*100
    else:
        score[i] = 100.
    total_sum += score[i]
print(total_sum/num_len)