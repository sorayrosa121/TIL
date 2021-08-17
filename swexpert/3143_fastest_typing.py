T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    repeat = 0      # b가 a내부에서 반복되는 횟수
    start = 0       # 시작 idx. b를 누를 수 있는 경우 b의 길이만큼 증가
    while start < (len(a) - len(b) + 1):
        if a[start:start+len(b)] == b:      # a의 (start번째~ +b길이까지)가 b와 같으면
            repeat += 1
            start += len(b)
        else:
            start += 1      # b가 a내부에서 반복되는 횟수 증가

    answer = len(a) - (len(b) * repeat) + repeat

    print(f'#{tc} {answer}')

# 5
# banana bana
# asakusa sa
# banana na
# banananana na
# abcabcabc abc
