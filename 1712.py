import math

def margin_number(a,b,c):
    if b >= c:
        return -1
    ans = math.floor(a/(c-b))
    return ans+1

a,b,c = map(float,input().split())
print(margin_number(a,b,c))