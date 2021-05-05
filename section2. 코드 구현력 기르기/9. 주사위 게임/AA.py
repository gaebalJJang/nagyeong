import sys
#sys.stdin=open("input.txt", "rt")

def prize(x, y, z):
    money = 0
    if x == y == z :
        money = 10000+(x*1000)
    elif x == y:
        money = 1000+(x*100)
    elif y == z:
        money = 1000+(y*100)
    elif x == z:
        money = 1000+(x*100)
    else:
        money = max(x, y, z)*100
        
    return money


n = int(input())
m = []

for i in range(n):
    x, y, z = map(int, input().split())
    m.append(prize(x,y,z))

print(max(m))
