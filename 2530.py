Arr = input().split()
H = int(Arr[0])
M = int(Arr[1])
S = int(Arr[2])
Add = int(input())
M_Add = (S + Add) // 60

A = (H + (M + M_Add) // 60) % 24
B = (M + M_Add) % 60
C = (S + Add) % 60

print(A,B,C)