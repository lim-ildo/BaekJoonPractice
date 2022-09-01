
p = int(input()) #참여하는 사람 수 3명
r = []
for i in range(p): # 3번 반복
    a, b, c = map(int,input().split()) #주사위 3개 눈 입력
    # 같은 눈 세 개
    if(a==b==c):
        result = 10000+(a*1000)

    #같은 눈 두 개
    elif(a==b):
        result = 1000+(a*100)
    elif(b==c):
        result = 1000+(b*100)
    elif(a==c):
        result = 1000+(a*100)

    #같은 눈이 없을 때
    else:
        li = []
        li.append(a)
        li.append(b)
        li.append(c)
        result = max(li)*100
    r.append(result)

print(max(r))


# person = int(input()) 
# answer = 0
# for _ in range(person): 
#     a, b, c = map(int, input().split()) 

#     if(a==b==c):
#         answer = max(answer, 10000+(a*1000))
#     elif(a==b):
#         answer = max(answer, 1000+(a*100))
#     elif(a==c):
#         answer = max(answer, 1000+(a*100))
#     elif(b==c):
#         answer = max(answer, 1000+(b*100))
#     else:
#         answer = max(answer, 100 * max(a,b,c))

# print(answer)
