import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int (input())
m = int (input())


for j in range (m) :
    for i in range (n) :
        print ("*",end="")
    print()
