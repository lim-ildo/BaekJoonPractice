sum = 0
for i in range(5):
    k = int(input())
    if k >= 40:
        k = k
        sum += k
    else:
        k = 40
        sum += k
print(int(sum/5))