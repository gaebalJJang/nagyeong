import sys
#sys.stdin=open("input.txt", "rt")

def reverse(x):
    a= list(map(int, str(x)))
    rev = 0
    for i in range(len(a)):
        rev += 10**(i) * a[i]
    return rev


def isPrime(x):
    for i in range(1, x+1):
        yaksu_num = 0
        for j in range(1, i+1):
            if i%j == 0:
                yaksu_num += 1
        
    if yaksu_num == 2:
        return True
    else:
        return False


n = int(input())
jayeonsu = list(map(int, input().split()))
print(jayeonsu)

ans = []
for i in range(n):
    num = reverse(jayeonsu[i])
    print(num)
    if isPrime(num):
        ans.append(num)

print(ans)
