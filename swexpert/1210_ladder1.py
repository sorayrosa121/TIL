T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점 찾기
    i = 99              # 가장 마지막 row이기 때문
    for x in range(100):
        if arr[99][x] == 2:
            j = x
            break       # 도착지점 column idx를 찾은 경우 for문 탈출

    while True:
        # 출발 지점(0번째 row)에 도착하면 멈춤
        if i == 0:
            break

        # 오른쪽 -> 위 방향 전환
        if j+1 < 100 and arr[i][j+1] == 1:  # col idx가 range(100)을 넘지 않고, 그 값이 1이면
            while j+1 < 100 and arr[i][j+1] == 1:
                j += 1                      # 오른쪽으로 감
            else:
                i -= 1                      # 오른쪽 경로가 없으면 위로 회전

        # 왼쪽 -> 위 방향 전환
        elif j > 0 and arr[i][j-1] == 1:    # col idx가 range(100)보다 작지 않고, 그 값이 1이면
            while j > 0 and arr[i][j-1] == 1:
                j -= 1                      # 왼쪽으로 감
            else:
                i -= 1                      # 왼쪽 경로가 없으면 위로 회전

        # 좌우 경로가 없는 경우 위로 직진
        else:
            i -= 1

    print(f'#{tc} {j}')