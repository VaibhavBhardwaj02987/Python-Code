import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a = input()
a = int (a)
b = input()
b = int (b)
c = input()
c = int (c)

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > b and c > a:
    print(c)


