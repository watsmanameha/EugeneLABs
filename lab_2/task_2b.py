N = 21
if N % 2 != 0 and 1 < N <= 100:
    two_dimensional_array = [[abs(i - j) + 1 for i in range(N)] for j in range(N)]
    final = []
    for row in two_dimensional_array:
        if two_dimensional_array.index(row) < N//2:
            final.append(row[:N//2] + row[N//2::-1])
        if two_dimensional_array.index(row) == N//2:
            final.append(row)
    for i in final[:N//2]:
        print(i)
    for i in final[::-1]:
        print(i)
