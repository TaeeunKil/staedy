T= int(input())
for i in range(1, T+ 1):
    T, T_end, k = input().split()
    T = float(T)
    T_end = float(T_end)
    k = float(k)

    count = 0
    while T > T_end:
        T *= k
        count += 1

    print(f"#{i} {count}")
