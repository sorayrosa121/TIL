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

        if left_two > 0 and left_one > 0 and right_two > 0 and right_one > 0: # 양 옆 두 칸 거리 이내 빌딩이 현 빌딩 높이보다 다 낮은 경우
            min_gap = min(left_two, left_one, right_two, right_one) # 최대로 확보된 조망권 확보 세대
            answer += min_gap
        else:
            continue
    
    print(f'#{tc} {answer}')