T=int(input())
for i in range(1,T+1):
    N,M=map(int,input().split())
    wi=list(map(int,input().split()))
    ti=list(map(int,input().split()))
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    sum=0
    count=0
    visit=[0]*len(ti)
    visit2=[0]*len(wi)
    for x in range(0,len(wi)):
        for y in range(0,len(ti)):
            if(wi[x]<=ti[y] and count<M and visit[y]!=1 and visit2[x]!=1):
                visit2[x]=1
                count+=1
                sum+=wi[x]
                visit[y]=1
    print(f'#{i} ',end='')
    print(sum)
