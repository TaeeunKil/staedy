T=int(input())
for i in range(1,T+1):
    A,B=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    co=0
    k=0
    if(A==B):
        for x in a:
            if(x in b):
                co+=1
        if(co==len(a)):
            print('=')
        else:
            k=1
    elif(A>B):
        for x in b:
            if(x in a):
                co+=1
        if(co==len(b)):
            print('>')
        else:
            k=1
    elif(A<B):
        for x in a:
            if(x in b):
                co+=1
        if(co==len(a)):
            print('<')
        else:
            k=1
    if k==1:
        print('?')
    