T=int(input())
for i in range(1,T+1):
    D,L,N=map(int,input().split())
    d=0
    for x in range(N):
        d+=D*(1+x*(L/100))
    print(f'#{i} ',end='')
    print(int(d))