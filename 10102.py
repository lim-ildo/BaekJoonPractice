P = int(input())

V = list(str(input()))
a = V.count('A')
b = V.count('B')
if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')
