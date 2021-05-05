import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
score = list(map(int, input().split()))

##평균 구하기
#전체값
sum = 0
for i in range(n):
    sum += score[i]
    
#평균(소수 첫째 자리에서 반올림)
med = round(sum/n)

#가까운 아이 구하기
num = 0
minus = med

for i in range(n):
    if abs(med-score[i]) <= minus:
        if score[num]<score[i]:
            num = i
            minus = abs(med-score[i])


print("%d %d" %(med, num+1))
