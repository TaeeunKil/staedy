def find():
    for x in range(N):
        for y in range(N):
            if(a[x][y])==2:
                end_x,end_y=x,y
                a[end_x][end_y]=0
            if(a[x][y])==3:
                start_x,start_y=x,y
                a[start_x][start_y]=0
    return end_x,end_y,start_x,start_y
from collections import deque
def bfs(start_x,start_y):
    q=deque()
    q.append((start_x,start_y))
    while q:
        x,y=q.popleft()
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if(0<=nx<N and 0<=ny<N and a[nx][ny]==0):
                a[nx][ny]=a[x][y]+1
                q.append((nx,ny))
T=int(input())
dx=[1,-1,0,0]
dy=[0,0,-1,1]
for i in range(1,T+1):
    N=int(input())
    a=[list(map(int,input().strip())) for _ in range(N)]
    end_x,end_y,start_x,start_y=find()
    bfs(start_x,start_y)
    print(f'#{i} ',end='')
    if(a[end_x][end_y]>=1):
        a[end_x][end_y]=a[end_x][end_y]-1
    print(a[end_x][end_y])
#