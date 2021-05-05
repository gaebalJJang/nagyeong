import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
ans = 0

#자연수의 수 만큼 루프 도는데
for i in range(1, n+1):
    yaksu_num = 0
    for j in range(1, i+1):
        if i%j == 0:
            yaksu_num += 1
    #소수는 나 자신과 1로만 나눠지니까 약수개수가 두개
    if yaksu_num == 2:
        ans += 1

print(ans)
