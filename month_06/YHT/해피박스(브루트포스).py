'''
박스에 N에 담길 최대 값만큼 Si를 담고 그거에 Pi 값을 계산하기
combinations?
'''
from itertools import combinations
T=int(input())
for i in range(1,T+1):
    N,M=map(int,input().split())
    q=[]
    p=[]
    o=[]
    sum2=[]
 
    for x in range(M):
        Si,Pi=map(int,input().split())
        q.append((Si,Pi))
    
    for y in range(1,len(q)+1):
        for x in combinations(q,y):
            sum3=0
            sum4=0
            for d,f in x:
                sum3+=d
                sum4+=f
                if(sum3<=N):
                    sum2.append(sum4)
    print(max(sum2))
        



            

    # for x in o:
    #     if(sum(x)==)
        
