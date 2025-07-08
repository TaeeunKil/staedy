T=10
for i in range(1,T+1):
    N=int(input())
    a=list(map(str,input().split()))
    b=int(input())
    c=list(map(str,input().split()))
    for x in range(len(c)):
        if(c[x]=='I'):
            d=int(c[x+1])
            e=int(c[x+2])
            for z in range(x+e+2,x+2,-1):
                a.insert(d,int(c[z]))
        if(c[x]=='D'):
            v=int(c[x+1])
            m=int(c[x+2]) 
            for p in range(v,v+m):
                a.pop(v)         
    print(f'#{i} ',end='')
    print(*a[0:10])
        
