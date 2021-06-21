dummy = []
for i in range(10):
    a = int(input())
    rest = a%42
    if rest not in dummy:
        dummy.append(rest)
print(len(dummy))