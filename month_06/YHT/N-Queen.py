"""
백트레킹 문제 N-Queen
행,열,대각선 놓을수 없다
8개 놓기 근데? 공격 안됨
"""
# def check(N,a,x,y,sum,result,dx,dy):
#     if(sum==N):
#         return result+1
#     if x >= N or y >= N:  # 인덱스 벗어나면 종료
#         return result
#     for w in range(x):
#         for z in range(y):
#             if(a[w][y]==1):
#                 return result
#             if(a[x][z]==1):
#                 return result
#             #대각선 추가해야함
#     for o in range(1,N):
#         for k in range(2):
#             nx=o*dx[k]+x
#             ny=o*dy[k]+y
#             if 0 <= nx < N and 0 <= ny < N:
#                 if a[nx][ny] == 1:
#                     return result
#     a[x][y] = 1
#     res1 = check(N, a, x + 1, 0, sum + 1, result, dx, dy)
#     a[x][y] = 0
#     res2 = check(N, a, x, y + 1, sum, result, dx, dy)
#     return res1 +res2 

# T=int(input())
# dx=[-1,-1]
# dy=[-1,1]
# for i in range(1,T+1):
#     result=0
#     sum=0
#     N=int(input())
#     a=[[0]*N for _ in range(N)]
#     check(N,a,0,0,sum,result,dx,dy)
#     print(result)

"""
다르게 생각 dfs로
v1,v2,v3
"""


def dfs(n):
    global ans
    if n==N:    # N행까지 진행한 경우 경우의수 가능: 성공
        ans+=1
        return

    for j in range(N):
        if v1[j]==v2[n+j]==v3[n-j]==0:  # 열/대각선 모두 Q없음
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0
T=int(input())
for i in range(1,T+1):

    N = int(input())
    ans = 0
    v1 = [0]*N
    v2 = [0]*(2*N)
    v3 = [0]*(2*N)
    dfs(0)
    print(f'#{i} ',end='')
    print(ans)


"""
3일뒤에 또 풀어보기
"""