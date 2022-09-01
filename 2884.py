H, M = map(int, input().split())
if H > 23:
    H = (H-24)

if H < 0:
    H = (H + 24)

elif 0 <= M < 60:
    M = (M-45)
    if M < 0:
        H = (H-1)
        if H < 0:
            H = H+24
        M = (M + 60)
    
elif M > 59:
    H=(H+1)
    M=(M-60)

print(H, M)

# if M > 44:
#     print(H, M-45)
# elif M < 45 and H > 0:
#     print(H-1,M+15)
# else:
#     print(23, M+15)