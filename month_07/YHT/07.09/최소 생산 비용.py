'''
DFS로 해보기
'''
# def dfs(x, y, count):
#     global sum2
#     for v in range(N):
#         visit[x][v] = 1
#     for v in range(N):
#         visit[v][y] = 1
#     sum2 += a[x][y]
#     count += 1

#     if count == N:
#         q.append(sum2)
#     else:
#         for z in range(N):
#             for l in range(N):
#                 if visit[z][l] == 0:
#                     dfs(z, l, count)

#     # 백트래킹
#     sum2 -= a[x][y]
#     for v in range(N):
#         visit[x][v] = 0
#     for v in range(N):
#         visit[v][y] = 0
def dfs(level,total):
    global min_cost
    if(total>=min_cost):
        return
    if(level==N):
        min_cost=min(min_cost,total)
        return

    for i in range(N):
        if(visit[i])==0:
            visit[i]=1
            dfs(level+1,total+a[level][i])
            visit[i]=0

T=int(input())
for i in range(1,T+1):
    N=int(input())
    a=[list(map(int,input().split())) for _ in range(N)]
    visit=[0]*N
    min_cost=float('inf')
    dfs(0,0)
    print(f'#{i} ',end='')
    print(min_cost)


