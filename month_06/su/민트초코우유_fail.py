# [삼성 기출 - 2025 상반기 오전 1번 문제] https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description
# 에러 코드

from pprint import pprint
from collections import deque
from collections import defaultdict

N, T = map(int, input().split())
food_board = [list(input()) for _ in range(N)] 
b_board = [list(map(int, input().split())) for _ in range(N)] # 헷갈림

sum_x_by_group = {
    "TCM": 0,
    "TC": 0,
    "TM": 0,
    "CM": 0,
    "M": 0,
    "C": 0,
    "T": 0,
}
leaders = [[] for _ in range(3)]  # 단일, 이중, 삼중

# 위 아래 왼쪽 오른쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# T민트 C초코 M우유
# T C M
# CM TM TC
# TCM

# 전파 그룹과 출력 그룹이 다름

spread_idx = {
    "T": 1,
    "C": 1,
    "M": 1,
    "CM": 2,
    "TM": 2,
    "TC":  2,
    "TCM": 0,
}

def convert_food(food_str, new_food):
    new_food_str = "".join(list(set(food_str + new_food)))  # 중복 제거
    if len(new_food_str) == 2:
        if "T" and "C" in new_food_str:
            new_food_str = "TC"
        elif "T" and "M" in new_food_str:
            new_food_str = "TM"
        elif "C" and "M" in new_food_str:
            new_food_str = "CM"
    elif len(new_food_str) == 3:
        new_food_str = "TCM"
    return new_food_str

for t in range(T):
    # 아침 시간
    for i in range(N):
        for j in range(N):
            b_board[i][j] += 1
            
    # 점심시간: 그룹 선정, 대표자 선정.
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            candidate = []
            visited[i][j] = 1
            candidate.append((-1 * b_board[i][j], i, j))  # 해당 그룹 내에서 대표자 선정하기 위해서 우선 모든 그룹원들을 넣는다.
            b_board[i][j] -= 1  
            cur_food = food_board[i][j]  

            queue.append((i, j))
            while queue:  # 그룹 형성
                row, col = queue.popleft()
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]
                    if nr < 0 or nc < 0 or nr >= N or nc >= N:
                        continue
                    if visited[nr][nc] or food_board[nr][nc] != cur_food:
                        continue
                    visited[nr][nc] = 1
                    candidate.append((-1 * b_board[nr][nc], nr, nc))
                    b_board[nr][nc] -= 1
                    queue.append((nr, nc))
            
            # 대표자 선정, 신앙심 몰아주기
            leader = sorted(candidate)[0]
            leader_b, leader_row, leader_col = leader
            b_board[leader_row][leader_col] += len(candidate)  # queue 탐색하면서 리더도 -1 했었으므로 -1은 다시 하지 않는다.
            leaders[spread_idx[cur_food]].append((-1 * b_board[leader_row][leader_col], leader_row, leader_col, cur_food))  
            
            sum_x_by_group[cur_food] += b_board[leader_row][leader_col] + len(candidate)  # 신앙심 총 합 기록
    
    # 저녁시간: 전파
    shield_mode = defaultdict(int)
    for i in range(3):  # 단일, 이중, 삼중 조합 순
        if not leaders[i]:  # 비어있는 경우 넘기기
            continue
        
        leaders[i].sort()
        # 단일 / 이중 / 삼중 그룹별 진행
        for j in range(len(leaders[i])):
            leader_b, leader_row, leader_col, leader_food = leaders[i][j]  # 대표자 선정. 음식.
            leader_b *= -1  # 다시 양수로 변환

            if shield_mode[(leader_row, leader_col)]:  # 리더가 다른 음식의 대표자에게 이미 전파 당한 경우 전파하지 않는다.
                continue

            # 전파 시작
            x = leader_b - 1  # 간절함으로 전환
            x_dir = x % 4  # 위 아 왼 오
            
            while x > 0:
                nr = leader_row + dr[x_dir]
                nc = leader_col + dc[x_dir]
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    break  # 전파 종료 (다음 그룹 전파 시작하기)
                if food_board[nr][nc] == cur_food:
                    leader_row, leader_col = nr, nc
                    continue  # 다음 칸 전파

                # 전파
                if x > b_board[nr][nc]:  # 강한 전파
                    sum_x_by_group[food_board[nr][nc]] -= b_board[nr][nc]   # 기존 음식은 신앙심 차감

                    food_board[nr][nc] = leader_food  # 새로운 음식으로 변경
                    x -= b_board[nr][nc] + 1  # 전파자 간절함 깎기
                    b_board[nr][nc] += 1  # 전파 대상 신앙심 증가

                    sum_x_by_group[food_board[nr][nc]] += b_board[nr][nc]  # 새로운 음식으로 신앙심 합계 업데이트

                    # 전파 후 간절함 0이면 전파 종료
                else:  # 약한 전파
                    sum_x_by_group[food_board[nr][nc]] -= b_board[nr][nc]   # 기존 음식은 신앙심 차감

                    new_food = convert_food(food_board[nr][nc], leader_food)
                    food_board[nr][nc] = new_food  # 전파
                    b_board[nr][nc] += x  # 전파 대상의 신앙심은 x만큼 증가

                    sum_x_by_group[food_board[nr][nc]] += b_board[nr][nc]  # 새로운 음식으로 신앙심 합계 업데이트

                    shield_mode[(nr, nc)] = 1  # 방어 상태 추가
                    break  # 더이상 전파를 진행하지 않는다.
                leader_row, leader_col = nr, nc

        # 저녁 시간 끝, 신앙심 총합 출력
        # 신앙심 총합 출력할때는 출력 그게 또 다름.... 
        for key, item in sum_x_by_group.items():
            print(key, item, end=", ")
            
        print()