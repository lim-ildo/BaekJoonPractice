Arr = input().split()
A = int(Arr[0])
B = int(Arr[1])
C = int(Arr[2])

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)