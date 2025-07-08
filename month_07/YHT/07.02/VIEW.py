T=10
for i in range(1,T+1):
    N=int(input())
    a=list(map(int,input().split()))
    sum=0
    for x in range(2,len(a)-2):
        b=a[x+1:x+3]
        c=a[x-2:x]
        if(max(b)<a[x] and max(c)<a[x]):
            sum+=a[x]-max(a[x-2],a[x-1],a[x+1],a[x+2])
    print(f'#{i} ',end='')
    print(sum)