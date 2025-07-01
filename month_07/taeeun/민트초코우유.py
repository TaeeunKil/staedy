# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description
from collections import deque
N, T = map(int, input().split())

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def find_groups(N, taste_map):
    visited = [[False]*N for _ in range(N)]
    groups = []

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                t = taste_map[i][j]
                q = deque([(i, j)])
                grp = [(i, j)]

                while q:
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and taste_map[nr][nc] == t:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                            grp.append((nr, nc))
                groups.append(grp)
    return groups

def representative(classroom, groups):

    reps = []

    for grp in groups:
        rep_r, rep_c = grp[0]
        max_belief = classroom[rep_r][rep_c]
        for r, c in grp[1:]:
            b = classroom[r][c]
            if b > max_belief or (b == max_belief and (r < rep_r or (r == rep_r and c < rep_c))):
                rep_r, rep_c, max_belief = r, c, b

        size = len(grp)
        for r, c in grp:
            if (r, c) != (rep_r, rep_c):
                classroom[r][c] -= 1
        classroom[rep_r][rep_c] += size - 1

        reps.append((rep_r, rep_c))

    return reps

def propagate_night(N, taste_map, classroom, reps):
 
    print(*res)



taste_map = [list(input()) for _ in range(N)]
classroom = [list(map(int, input().split())) for _ in range(N)]


for day in range(1, T+1):
    print(classroom)
    # morning
    for i in range(N):
        for j in range(N):
            classroom[i][j] += 1
    # afternoon
    groups = find_groups(N, taste_map)
    reps   = representative(classroom, groups)
    print(classroom)
    
    # night
    propagate_night(N, taste_map, classroom, reps)


