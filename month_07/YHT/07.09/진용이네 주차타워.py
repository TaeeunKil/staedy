'''
와 무려 2일을 고민해서 풀었다 헤헤
런탄ㄴ잉ㄴㅇㄴ멀냘널ㄴ머랜매;런;ㄹ

'''
# def check(level):
#     global total
#     if len(q) == 0 or level >= len(q):
#         return

#     for x in range(len(p)):
#         if p[x] == 0 and q[level] > 0:
#             p[x] = q[level]
#             q.pop(level)
#             check(0)
#             return

#     if q[level] < 0:
#         for x in range(len(p)):
#             if abs(q[level]) == p[x]:
#                 total += Ri[x] * Wi[abs(q[level]) - 1]
#                 p[x] = 0
#                 q.pop(level)
#                 check(0)
#                 return

#     if level + 1 < len(q):  
#         check(level + 1)



# T=int(input())
# for i in range(1,T+1):
#     n,m=map(int,input().split())
#     Ri=[]
#     Wi=[]
#     q=[]
#     p=[0]*n
#     total=0
#     for x in range(n):
#         Ri.append(int(input()))
#     for x in range(m):
#         Wi.append(int(input()))
#     for x in range(2*m):
#         q.append(int(input()))

#     check(0)
#     print(f'#{i} ',end='')
#     print(total)


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    Ri = [int(input()) for _ in range(n)]      # 주차공간 단위요금
    Wi = [int(input()) for _ in range(m)]      # 차량 무게
    q = [int(input()) for _ in range(2 * m)]   # 차량 입출차 순서

    p = [0] * n          # 주차장 상태
    pos = [0] * (m + 1)  # 차량번호 위치 매핑
    wait = []            # 대기 큐
    total = 0

    for car in q:
        if car > 0:
            # 입차 요청
            parked = False
            for i in range(n):
                if p[i] == 0:
                    p[i] = car
                    pos[car] = i
                    total += Ri[i] * Wi[car - 1]
                    parked = True
                    break
            if not parked:
                wait.append(car)

        else:
            # 출차 요청
            car = -car
            i = pos[car]
            p[i] = 0

            # 자리 비었으니 대기 중인 차 먼저 입차
            if wait:
                next_car = wait.pop(0)
                p[i] = next_car
                pos[next_car] = i
                total += Ri[i] * Wi[next_car - 1]

    print(f'#{tc} {total}')
