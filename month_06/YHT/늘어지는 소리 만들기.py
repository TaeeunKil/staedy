"""
코딩 감 되찾기 연습중
그냥 해당 값에 - 추가하는 문제

"""
T=int(input())
for i in range(1,T+1):
    a=list(map(str,input().strip()))
    b=int(input())
    c=list(map(int,input().split()))
    c.sort(reverse=True)
    d='-'
    for x in range(len(c)):
        a.insert(c[x],d)
    print(f'#{i} ',end='')
    for x in range(len(a)):
        print(a[x],end='')
    print()
    