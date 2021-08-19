def dfs(arr1, arr2):
    stack = []
    visited = [0] * 100
    now = 0 # START
    visited[0] = 1

    while now > -1:
        if now == 99:   # END 노드까지 도달한 경우
            return 1

        if arr1[now] != -1 and visited[arr1[now]] < 3:      # arr1에서 0과 인접하고(-1이 아니고) 최대 두 번까지만 방문한 경우
            stack.append(arr1[now])
            now = arr1[now]
            visited[now] += 1
        elif arr2[now] != -1 and visited[arr2[now]] < 3:    # arr1에서 0과 인접하고(-1이 아니고) 최대 두 번까지만 방문한 경우
            stack.append(arr2[now])
            now = arr2[now]
            visited[now] += 1
        else:
            if stack:   # 아직 후진 가능한 경우
                now = stack.pop()   # 다시 노드를 꺼내 now 지정

            else:   # 후진 불가능한 경우
                return 0
    return 0

T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    arr1 = [-1] * 100   # 정점 번호를 주소로 사용하는 배열 1
    arr2 = [-1] * 100   # 정점 번호를 주소로 사용하는 배열 2
    A = list(map(int, input().split()))     # 정점들의 순서쌍 나열

    for i in range(0, 2*E, 2):              # 순서쌍이므로 E * 2개
        a, b = A[i], A[i+1]
        if arr1[a] == -1:   # 만약 arr1에 아직 저장되지 않은 정점인 경우
            arr1[a] = b
        else:               # arr1 주소에는 저장된 정점인 경우
            arr2[a] = b

    answer = dfs(arr1, arr2)
    print(f'#{tc} {answer}')
