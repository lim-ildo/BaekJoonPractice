N = int(input())
for _ in range(N):
    Arr = input().split()
    R = int(Arr[0])
    S = Arr[1]
    temp = ''
    for i in range(len(S)):
        temp += S[i]*R
    print(temp)