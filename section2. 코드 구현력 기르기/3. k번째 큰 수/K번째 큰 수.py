import sys
sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
res=set()   #3장 더한 값 저장  

#3개를 뽑을 수 있는 모든 경우의 수
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)

#기록한 값 중 k번째로 큰 수
print(res[k-1])
