T = int(input())

for i in range(T):
    Arr = input().split()
    A = int(Arr[0])
    B = int(Arr[1])
    print('Case #%d: %d + %d = %d' %((i+1), A, B, (A+B)))