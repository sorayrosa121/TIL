def find_route(i, j, k, l):
    if i == k and j == l:
        return 1
    else:
        arr[i][j] = 1
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # 4방향 탐색 (위, 오른쪽, 아래, 왼쪽)
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
                if find_route(ni, nj, k, l):    # 출구를 찾고 리턴하면
                    return 1
        return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input()] for _ in range(N)]
    # 0은 통로, 1은 벽, 2는 출발, 3은 도착
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 2:
                i, j = a, b
            elif arr[a][b] == 3:
                k, l = a, b


    answer = find_route(i, j, k, l)

    print(f'#{tc} {answer}')