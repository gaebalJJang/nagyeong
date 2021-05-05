import sys
#sys.stdin=open("input.txt", "rt")

def upsidedownsame(x):
    ans = "YES"
    for i in range(len(x)//2):
        if x[i] != x[-1-i]:
            ans = "NO"
            break
    return ans


n = int(input())
a = []

for i in range(n):
    word=input()
    word = word.upper()
    result = upsidedownsame(word)
    print("#%d %s" %(i+1, result))
   
  
    
    
