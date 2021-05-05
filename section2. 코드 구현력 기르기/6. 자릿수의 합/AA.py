import sys
#sys.stdin=open("input.txt", "rt")

def digit_sum(x):
    return sum(map(int, str(x)))


n = int(input())
l = list(map(int, input().split()))
max_num = 0
max_int = 0

for i in range(n):
    if max_int < digit_sum(l[i]):
        max_int = digit_sum(l[i])
        max_num = i

print(l[max_num])
