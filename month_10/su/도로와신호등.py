import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline


N, L = map(int, input().split())
lights = [tuple(map(int, input().split())) for _ in range(N)]
lights.sort(key=lambda x: x[0])  # D 기준 정렬(안전)

t = 0       # 현재 시간
pos = 0     # 현재 위치

for D, R, G in lights:
    # 신호등까지 이동
    t += D - pos  # 걸린 시간
    pos = D  # 

    # 바로 출발해도 되는지 확인
    cycle = (R + G)
    phase = t % cycle
    if phase < R:
        rest_p = R - phase
        t += rest_p

# 종점까지
t += L - pos
print(t)
