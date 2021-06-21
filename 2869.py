import math

def snail(a,b,c):
    return math.ceil((c-a)/(a-b))+1

a,b,c = map(float, input().split())
print(snail(a,b,c))