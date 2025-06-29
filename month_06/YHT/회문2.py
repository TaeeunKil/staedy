'''
가로 세로 직선이 되는 가장 긴 회문 찾기
'''
T=10
def check(li):
    sum2=0
    for z in range(100):
        for x in range(100,0,-1):
            for y in range(100-x+1):
                s=li[z][y:y+x]
                if(s==s[::-1]):
                    sum2=max(sum2,x)
                    break
    return sum2


for i in range(1,T+1):
    z=int(input())
    a=[list(map(str,input().strip())) for _ in range(100)]
    b=list(zip(*a))
    max2=check(a)
    max3=check(b)
    max4=max(max2,max3)
    print(f'#{z} ',end='')
    print(max4)

    
        