"""
A와 B가 서로를 향해 달리고 있고 전면부는 250마일 
A는 시속 10마일 B는 시속 15마일
파리가 a에서 출발하는데 b에 닿으면 바로 방향 바꿔서 a한테 감
몇마일 이동했냐
뭔가 리스트로 하고싶은데? 필요없네
기차가 리스트로 지나온곳을 다 1로 만들고
에라이 그냥 간단한 문제였네
"""
# def check(A,B,t,D):
#     a,b=t*A,D-t*B
#     return a,b
# def fari(dir,F,a,b,sum,t,d):
#     if(dir==0):
#         sum+=F
#         if(t*F==b):
#             d=b
#             return dir+1,sum,d
#         else:
#             return dir,sum,d
#     else:
#         sum+=F
#         d=d-t*F
#         if(d==a):
#             return dir-1,sum
#         else:
#             return dir,sum


# T=int(input())
# for i in range(1,T+1):
#     D,A,B,F=map(int,input().split())
#     t=0
#     k=D/(A+B)
#     sum=0
#     d=0
#     dir=0
#     while t<k:
#         t+=1
#         a,b=check(A,B,t,D)
#         dir,sum,d=fari(dir,F,a,b,sum,t,d)
#     print(f'#{i} ',end='')
#     print(sum) 
        

T = int(input())
for i in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    t = D / (A + B)
    result = F * t
    print(f"#{i} {result}")

