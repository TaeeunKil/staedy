from collections import deque

def solution(maze):
    m, n = len(maze), len(maze[0])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    red = blue = None
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 1:
                red = (i, j)
            elif maze[i][j] == 2:
                blue = (i, j)

    visited = [[[[False] * n for _ in range(m)] for _ in range(n)] for _ in range(m)]

    q = deque()
    q.append((red[0], red[1], blue[0], blue[1], 0))
    visited[red[0]][red[1]][blue[0]][blue[1]] = True

    while q:
        rr, rc, br, bc, cnt = q.popleft()

        # 둘 다 도착했으면 종료
        if maze[rr][rc] == 3 and maze[br][bc] == 4:
            return cnt

        red_goal = (maze[rr][rc] == 3)
        blue_goal = (maze[br][bc] == 4)

        r_moves = []
        b_moves = []

        if red_goal:
            r_moves.append((rr, rc))
        else:
            for d in range(4):
                nrr, nrc = rr + dr[d], rc + dc[d]
                if 0 <= nrr < m and 0 <= nrc < n and maze[nrr][nrc] != 5:
                    r_moves.append((nrr, nrc))
            if not r_moves:
                r_moves.append((rr, rc))  # 이동 못하면 제자리

        if blue_goal:
            b_moves.append((br, bc))
        else:
            for d in range(4):
                nbr, nbc = br + dr[d], bc + dc[d]
                if 0 <= nbr < m and 0 <= nbc < n and maze[nbr][nbc] != 5:
                    b_moves.append((nbr, nbc))
            if not b_moves:
                b_moves.append((br, bc))  # 이동 못하면 제자리

        for nrr, nrc in r_moves:
            for nbr, nbc in b_moves:
                # 겹침 방지
                if (nrr, nrc) == (nbr, nbc):
                    continue
                # 스위칭 방지
                if (nrr, nrc) == (br, bc) and (nbr, nbc) == (rr, rc):
                    continue
                if not visited[nrr][nrc][nbr][nbc]:
                    visited[nrr][nrc][nbr][nbc] = True
                    q.append((nrr, nrc, nbr, nbc, cnt + 1))

    return 0