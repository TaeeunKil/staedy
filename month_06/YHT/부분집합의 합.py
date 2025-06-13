"""
부분 집합의 개수를 구하는 거임 모든 부분집합을 찾아 답을 찾자 그냥

"""
from itertools import combinations

T=int(input())

for i in range(1,T+1):
    N,K=map(int,input().split())
    result=0
    q=[]
    for y in range(1,N+1):
        for x in combinations(range(1,13),y):
            q.append(x)
    for x in range(len(q)):
        if(sum(q[x])==K and len(q[x])==N):
            result+=1
    print(f'#{i} ',end='')
    print(result)