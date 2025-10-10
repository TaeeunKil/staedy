import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline


from collections import Counter


N, K = map(int, input().split())
data = []
key = ()
for i in range(N):
    idx, gold, silver, bronze = map(int, input().split())
    if idx == K:
        key = (gold, silver, bronze)

    data.append((gold, silver, bronze))

counter_data = Counter(data)
sorted_data = sorted(counter_data.items(), key=lambda x: x[0],  reverse=True)


prev_score = ()

i = 0
last_ranking = 0
while i < len(sorted_data):

    if sorted_data[i][0] == key:
        print(last_ranking + 1)
        break

    last_ranking += sorted_data[i][1]
    i += 1