import sys
sys.stdin=open("input.txt", "rt")     #파일을 입출력하기 위해

n, k = map(int, input().split())    #map을 이용하여 두가지 숫자를 한번에 입력받음
cnt = 0     #갯수를 세기 위한 변수

for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
    #k번째 약수가 발견하지 못했을때는 -1을 해줘야 함
else:      #정상적으로 for문이 돌았을때는 else문을 수행하지 않음
    print(-1)
