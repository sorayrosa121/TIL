T = int(input())
# 오른쪽, 아래, 왼쪽, 위(우측 90도 회전)
di = [0, 1, 0, -1] 
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]   # N * N 이차원 배열의 모든 초기값 0

    cnt = 1     # 1씩 증가하며 각 배열에 입력될 값
    i, j = 0, -1 # 시작 위치 idx
    k = 0 # (di, dj) 방향 전환을 위한 key
    while cnt <= N * N:     # N * N개가 채워질 때까지
        ni, nj = i+di[k], j+dj[k]   # 다음번 행, 열 idx
        # if ni, nj가 0이상 N미만이고, A[ni][nj]가 아직 초기값(0)에서 변경되지 않은 상태라면,
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt   # cnt값을 (ni, nj)번째에 할당
            cnt +=1
            i, j = ni, nj   # 현 위치 변경
        else:   # N * N 배열의 끝에 도달하거나, 이미 변경된 값이면
            k = (k+1) % 4 # 나머지 값으로 (di, dj) 4개 중 한 방향으로 순환

    print(f'#{tc}')
    for rows in arr:
        print(*rows) # list unpack asterisk
