# [삼성 기출 - 2025 상반기 오전 1번 문제] https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description

# 변수가 많아서 덮어쓰거나 혼용하는 실수가 많았음
# i, j 전역변수 덮어쓰기 오류
# 방향: x가 아닌 B를 4로 나눴어야 한다
# leader_food != cur_food
# x와 b를 따로 갱신하지 않는다.
# 문제 잘읽기: 약한 전파든 강한 전파든 전파당하면 방어 상태되는 것임
# "T" and "C" in new_food_str (X), "T" in new_food_str and "C" in new_food_str (O)

from pprint import pprint
from collections import deque
from collections import defaultdict

N, T = map(int, input().split())
food_board = [list(input()) for _ in range(N)] 
b_board = [list(map(int, input().split())) for _ in range(N)]

# 위 아래 왼쪽 오른쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 전파 그룹과 출력 그룹이 다름
spread_idx = {
    "T": 0,
    "C": 0,
    "M": 0,
    "CM": 1,
    "TM": 1,
    "TC":  1,
    "TCM": 2,
}

def convert_food(food_str, new_food):
    new_food_str = "".join(list(set(food_str + new_food)))  # 중복 제거
    if len(new_food_str) == 2:
        if "T" in new_food_str and "C" in new_food_str:
            new_food_str = "TC"
        elif "T" in new_food_str and "M" in new_food_str:
            new_food_str = "TM"
        elif "C" in new_food_str and "M" in new_food_str:
            new_food_str = "CM"
    elif len(new_food_str) == 3:
        new_food_str = "TCM"
    return new_food_str

for t in range(T):
    # 아침 시간
    for r in range(N):
        for c in range(N):
            b_board[r][c] += 1
    # 점심시간: 그룹 선정, 대표자 선정.
    leaders = [[] for _ in range(3)]  # 단일, 이중, 삼중
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            candidate = []
            visited[i][j] = 1
            candidate.append((-1 * b_board[i][j], i, j))  # 해당 그룹 내에서 대표자 선정하기 위해서 모든 그룹원들을 넣어 나갈 것임.
            b_board[i][j] -= 1  
            cur_food = food_board[i][j]  

            queue.append((i, j))
            while queue:  # 그룹 형성
                row, col = queue.popleft()
                for k in range(4):
                    nr = row + dr[k]
                    nc = col + dc[k]
                    if nr < 0 or nc < 0 or nr >= N or nc >= N:
                        continue
                    if visited[nr][nc] or food_board[nr][nc] != cur_food:
                        continue
                    visited[nr][nc] = 1
                    candidate.append((-1 * b_board[nr][nc], nr, nc))  # 음수로 변환해서 넣는다.
                    b_board[nr][nc] -= 1
                    queue.append((nr, nc))
            
            # 대표자 선정, 신앙심 몰아주기
            leader = sorted(candidate)[0]
            _, leader_row, leader_col = leader  
            b_board[leader_row][leader_col] += len(candidate)  # queue 탐색하면서 리더도 -1 했었으므로 -1은 다시 하지 않는다.
            leaders[spread_idx[cur_food]].append((-1 * b_board[leader_row][leader_col], leader_row, leader_col, cur_food))  
            
    
    # 저녁시간: 전파
    shield_mode = defaultdict(int)
    for combi_i in range(3):  # 단일, 이중, 삼중 조합 순
        if not leaders[combi_i]:  
            continue
        leaders[combi_i].sort()  # 정렬해서 순서대로 전파 진행한다. (전파력, row, col 순)
        # 단일 / 이중 / 삼중 그룹별 진행
        for group_i in range(len(leaders[combi_i])):
            leader_b, leader_row, leader_col, leader_food = leaders[combi_i][group_i]  
            leader_b *= -1  # 다시 양수로 변환

            if shield_mode[(leader_row, leader_col)]:  # 리더가 다른 음식의 대표자에게 이미 전파 당한 경우 전파하지 않는다.
                continue

            # 전파 시작
            b_board[leader_row][leader_col] = 1  # 전파자는 신앙심 중 1만 남는다.
            x = leader_b - 1  # 나머지는 간절함으로 전환
            b_dir = leader_b % 4  # 위 아 왼 오  
            
            while x > 0:
                nr = leader_row + dr[b_dir]
                nc = leader_col + dc[b_dir]
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    break  # 전파 종료 (다음 그룹 전파 시작하기)
                if food_board[nr][nc] == leader_food:
                    leader_row, leader_col = nr, nc
                    continue  # 그 다음 칸 확인 필요

                # 전파
                if x > b_board[nr][nc]:  # 강한 전파
                    food_board[nr][nc] = leader_food  # 새로운 음식으로 변경
                    x -= b_board[nr][nc] + 1  #  간절함 깎기
                    b_board[nr][nc] += 1  # 전파 대상 신앙심 증가
                    shield_mode[(nr, nc)] = 1  # 방어 상태 추가
                else:  # 약한 전파
                    new_food = convert_food(food_board[nr][nc], leader_food)
                    food_board[nr][nc] = new_food  # 새로운 음식으로 변경
                    b_board[nr][nc] += x  # 전파 대상의 신앙심은 x만큼 증가
                    shield_mode[(nr, nc)] = 1  # 방어 상태 추가
                    x = 0
                    break  # 더이상 전파를 진행하지 않는다.
                leader_row, leader_col = nr, nc

    # 저녁 시간 끝, 신앙심 총합 출력
    sum_b_by_group = {
        "TCM": 0,
        "TC": 0,
        "TM": 0,
        "CM": 0,
        "M": 0,
        "C": 0,
        "T": 0,
    }
    for food_row in range(N):
        for food_col in range(N):
            sum_b_by_group[food_board[food_row][food_col]] += b_board[food_row][food_col]
    
    for key, item in sum_b_by_group.items():
        print(item, end=" ")
    print()