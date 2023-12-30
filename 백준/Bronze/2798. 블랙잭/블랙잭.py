import sys

N, M = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            result = cardList[i] + cardList[j] + cardList[k]
            if M == result:
                ans = result
                break
            elif result < M and abs(M - result) < abs(M - ans):
                ans = result
        if M == ans and result < M:
            break
    if M == ans and result < M:
        break
    
print(ans)