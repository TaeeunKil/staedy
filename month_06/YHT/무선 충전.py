"""
초기도 충전가능함

T를 +1씩 더해가면서 4방 탐색으로 이동정보로 이동하고
들어갈 수 있는 곳을 A,B list으로 하고 같은게 있으면 둘중 다른곳을 갈수있으면
그걸로 들어가게 하고 충전값을 list 로 넣고 둘의 충전량을 더한다 
"""

# T=int(input())
# dx=[0,-1,0,1,0]
# dy=[0,0,1,0,-1]
# def moving(x,y,li,alpa):
#     global t
#     if(t>M):
#         return 
#     if(z[x][y]>=0):
#         alpa.append(z[x][y])
#     for v in li:
#         x=x+dx[v]
#         y=y+dy[v]
#         t=t+1
#         moving(x,y,li,alpa)

# def check(x1,y1,c1,p1):
#     for x in range(10):
#         for y in range(10):
#             if((abs(x-x1-1)+abs(y-y1-1))<=c1):
#                 z[x][y1].append(p1)
    
    


# for i in range(1,T+1):
#     M,e=map(int,input().split())
#     A=list(map(int,input().split()))
#     A_i=[]
#     B=list(map(int,input().split()))
#     B_i=[]
#     z = [[[] for _ in range(10)] for _ in range(10)]
#     t=0
#     for x in range(e):
#         y1,x1,c1,p1=map(int,input().split())
#         check(x1,y1,c1,p1)
#     print(z)




#못품
