import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
dap = list(map(int, input().split()))
yeonsok = 0
ans = 0


for i in range(n):
    
    if dap[i] == 1:
        yeonsok += 1
    else:
        yeonsok = 0
    ans += yeonsok   

print(ans)
