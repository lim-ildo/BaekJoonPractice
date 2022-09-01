P = int(input())
a = 0
b = 0
for _ in range(P):
    V = int(input())
    if V == 1:
        a += 1
    else :
        b += 1

if a > b:
    print("Junhee is cute!")
elif a < b:
    print("Junhee is not cute!")
else:
    print("..")