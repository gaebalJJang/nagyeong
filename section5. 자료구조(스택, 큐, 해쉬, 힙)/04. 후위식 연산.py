'''
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9을 후위연산식으로 표현하면352+*9-로 표현되며 그 결과는 21입니다.

'''

import sys

sys.stdin = open("in4.txt", "r")
input = input()
stack = []

for x in input:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            j = stack.pop()
            i = stack.pop()
            stack.append(i+j)
        elif x == '-':
            j = stack.pop()
            i = stack.pop()
            stack.append(i - j)
        elif x == '*' or x == '-':
            j = stack.pop()
            i = stack.pop()
            stack.append(i * j)
        elif x == '/':
            j = stack.pop()
            i = stack.pop()
            stack.append(i / j)
print(stack[0])
