B = list(str(input()))
answer = 0

for i in range(len(B)):
    if i == 0:
        answer += 10
    elif B[i] == B[i-1]:
        answer += 5
    else:
        answer += 10

print(answer)