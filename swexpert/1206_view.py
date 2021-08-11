T = 10 # 테스트 케이스 10개

for tc in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = 0 # 조망권이 확보된 총 세대 수
    for i in range(2, n-2):
        
        left_two = buildings[i] - buildings[i-2] # 왼쪽으로 2칸 거리 빌딩과의 높이차이
        left_one = buildings[i] - buildings[i-1] # 왼쪽으로 1칸 ~
        
        right_two = buildings[i] - buildings[i+2] # 오른쪽으로 2칸 ~
        right_one = buildings[i] - buildings[i+1] # 오른쪽으로 1칸 ~

        temp = []
        temp.append(left_two)
        temp.append(left_one)
        temp.append(right_two)
        temp.append(right_one)
        
        cnt = 0
        min_gap = temp[0]

        for x in temp:
            if x > 0:
                cnt += 1
                if min_gap > x: # 최대로 확보된 조망권 확보 세대
                    min_gap = x
        
        if cnt == 4: # 양 옆 두 칸 거리 이내 빌딩이 현 빌딩 높이보다 다 낮은 경우
            answer += min_gap

    print(f'#{tc} {answer}')