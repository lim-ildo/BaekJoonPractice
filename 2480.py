a, b, c = map(int,input().split())
# 같은 눈 세 개
if(a==b==c):
    print(10000+(a*1000))

#같은 눈 두 개
elif(a==b):
    if b!=c:
        print(1000+(a*100))
elif(b==c):
    if c!=a:
        print(1000+(b*100))
elif(a==c):
    if a!=b:
        print(1000+(a*100))

#같은 눈이 없을 때
else:
    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    print(max(li)*100)
