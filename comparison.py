import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a = input()
a = int (a)
b = input()
b = int (b)


if a > b :
    print (a)
elif a < b :
    print (b)
elif a == b :
    print ("both are equal")
