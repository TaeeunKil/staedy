import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

N = int(input())
score = [0, 0, 0]  # 1번팀 점수, 2번팀 점수
times = [0, 0, 0]  # 새로 이기기 시작한 시간 (초로 계산하기)
cur_winner = 0  # 
last_sec = 0

def get_sec(timezone):
    mm, ss = map(int, timezone.split(":"))
    seconds = 0
    seconds += mm * 60
    seconds += ss
    return seconds


def get_timezone(sec):
    mm, ss = sec // 60, sec % 60
    timezone = f"{mm:02d}:{ss:02d}"
    return timezone


for i in range(N):
    team, t = input().split()
    team = int(team)
    seconds = get_sec(t)
    gap = seconds - last_sec
    
    if cur_winner != 0:
        times[cur_winner] += seconds - last_sec  # 이전에 이기고 있던 팀에 시간 추가
    
    last_sec = seconds
    
    score[team] += 1  # 득점 추가
    
    # 리더 재 판정
    if score[1] > score[2]:
        cur_winner = 1
    elif score[1] < score[2]:
        cur_winner = 2
    else:
        cur_winner = 0


# 48:00일 때..
seconds = get_sec("48:00")
times[cur_winner] += seconds - last_sec  # 이전에 이기고 있던 팀에 시간 추가

# print(cur_winner)
for j in range(1, 3):
    print(get_timezone(times[j]))



# timezone = get_timezone(seconds)
# print(timezone)

# 골 들어오면 시간 차이 계산. 그리고 지금까지 이기고 있었던 팀에 += 1
# 새로 이기고 있던 팀 갱신하기
# 
#  

# import sys
# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
# sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
# input = sys.stdin.readline

# # 4:55~ 5:55
# # 팀 번호는 1 또는 2이다.
# # 첫째 줄에 1번 팀이 이기고 있던 시간, 둘째 줄에 2번 팀이 이기고 있던 시간 출력

# N = int(input())
# score = [0, 0, 0]  # 1번팀 점수, 2번팀 점수
# times = [0, 0, 0]  # 새로 이기기 시작한 시간 (초로 계산하기)
# cur_winner = -1  # 

# # winner가 바뀔 때 이전에 이기고 있던 팀 계산을 해줘야 한다.

# # 골 넣었을 때
# # 내가 이기고 있었던 경우
#     # 킵 고잉
# # 내가 지고 있었던 경우
#     # 이제부터 시간재야 한다.
# # 동점인 경우

# def get_sec(timezone):
#     mm, ss = map(int, timezone.split(":"))
#     seconds = 0
#     seconds += mm * 60
#     seconds += ss
#     return seconds


# def get_timezone(sec):
#     mm, ss = sec // 60, sec % 60
#     timezone = f"{mm:02d}:{ss:02d}"
#     return timezone


# for _ in range(N):
#     team, t = input().split()
#     team = int(team)
#     seconds = get_sec(t)
#     if cur_winner == team:
#         score[team] += 1
#         continue
#     else:  # 
#         score[team] += 1
#         cur_winner = team

#         if cur_winner != -1:  # 다른 팀이 이기고 있었을 때
#             score[team] += 1

#             other_team = 1  # 
#             if team == 1:
#                 other_team = 2


#             if score[team] > score[other_team]:  # 역전한 경우
#                 cur_winner = team
#                 # 이전까지 이기고 있던 팀 시간 계산

#             elif score[team] < score[other_team]:
#                 cur_winner = other_team
#             else:
#                 cur_winner = -1

        
#         else:  # 동점일 때
#             pass

# timezone = get_timezone(seconds)
# print(timezone)