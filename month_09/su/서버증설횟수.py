# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/389479?language=python3
# 2025 프로그래머스 코드챌린지 2차 예선

from collections import deque
def solution(players, m, k):
    answer = 0
    queue = deque()
    for i in range(24):
        if players[i] < m:  # m명 미만이라면, 서버 증설이 필요하지 않음
            continue
            
            
        while queue:
            if queue[0][0] <= i: # 이미 이 서버 시간 끝났으면 삭제하기
                queue.popleft()
            else:
                break
                
        server_len = len(queue)
        needed = players[i] // m
        gap = server_len - needed  # 새로 증설해야 하는 서버 수
        
        if gap < 0:  # 지금 있는 서버로는 부족한 경우에만 증설하기
            for j in range(abs(gap)):
                queue.append((i + k, i))  # 끝나는 시간, 시작한 시간
                answer += 1
        
    return answer