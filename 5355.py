T = int(input())

for i in range(T):
    M_sen = input().split()
    num = float(M_sen[0])
    for k in range(len(M_sen)):       
        if M_sen[k] == '@': num = num * 3
        elif M_sen[k] == '%': num = num + 5
        elif M_sen[k] == '#': num = num - 7
    print('%0.2f'%num)

