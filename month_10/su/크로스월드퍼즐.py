# https://www.acmicpc.net/problem/9626

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

board = [list(input().strip()) for _ in range(M)]

new_W, new_H = (N + L + R), (M + U + D)
new_board = [[""] * new_W for _ in range(new_H)]


for i in range(new_H):
    for j in range(new_W):
        if (i + j) % 2 == 0:
            new_board[i][j] = "#"
        else:
            new_board[i][j] = "."


# 원본 보드 덮기
for i in range(M):
    for j in range(N):
        new_board[i + U][j + L] = board[i][j]

for row in new_board:
    print("".join(row))