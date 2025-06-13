'''
가지치기 백트레킹 했지만 실패...100분을 갈았다...

'''

def dfs(x, y, N, visit3, sum, counts):
    if x >= N or y >= N:
        return
    if counts == N:
        z.append(sum)
        return

    if visit3[x][y] == 0:
        counts += 1
        sum += a[x][y]

        for i in range(N):
            visit3[x][i] = 1
            visit3[i][y] = 1


        visit2 = [[0]*(N-1) for _ in range(N-1)]
        coords = []
        n, m = 0, 0

        for i in range(N):
            for j in range(N):
                if visit3[i][j] == 0:
                    visit2[n][m] = a[i][j]
                    coords.append((i, j))  
                    n += 1
                    if n == N - 1:
                        n = 0
                        m += 1

        for nx, ny in coords:
            dfs(nx, ny, N, [row[:] for row in visit3], sum, counts)


T = int(input())

for i in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    z = []

    for x in range(N):
        for y in range(N):
            dfs(x, y, N, [row[:] for row in visit], 0, 0)

    if z:
        print(f'#{i} {min(z)}')
    else:
        print(f'#{i} No result')
