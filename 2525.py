Arr = input().split()
H = int(Arr[0])
M = int(Arr[1])
Add = int(input())

A = (H + ((M + Add) // 60)) % 24
B = (M + Add) % 60

print(A,B)