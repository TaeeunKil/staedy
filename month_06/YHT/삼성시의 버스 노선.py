T=int(input())
for i in range(1,T+1):
    a1=[]
    b1=[]
    N=int(input())
    for x in range(N):
        a,b=map(int,input().split())
        a1.append(a)
        b1.append(b)
    P=int(input())
    
    p=[]
    for x in range(P):
        k=int(input())
        p.append(k)
    print(f'#{i}',end=' ')
    for x in p:
        sun=0
        
        for y in range(N):
            if(a1[y]<=x<=b1[y]):
                sun+=1
        
        print(sun,end=' ')
    print()