T = 10
for tc in range(1, T+1):
    N = int(input())
    s1 =input()
    stack = []
    s2 = ''

    # step 1) 후위표기법으로 변환
    for x in s1:
        if '0' <= x <= '9': # 토큰이 피연산자이면
            s2 += x
        elif x == '*':      # 토큰이 우선순위가 더 높은 연산자 '*'인 경우
            stack.append(x)
        elif x == '+':      # 토큰이 우선순위가 더 낮은 연산자 '+'인 경우
            while stack:    # stack 비어있지 않은 동안
                s2 += stack.pop()   # 모두 꺼내기
            stack.append(x)
    while stack:            # stack에 남아있는 중위표기식이 있으면 모두 꺼내기
        s2 += stack.pop()

    # step 2) 후위표기법으로 변환한 식 계산
    for y in s2:
        if '0' <= y <= '9': # 토큰이 피연산자이면
            stack.append(y)
        elif y == '*':          # '*' 연산자이면, 해당 연산 결괏값을 stack에 push
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(int(op2) * int(op1))
        elif y == '+':          # '+' 연산자이면, 해당 연산 결괏값을 stack에 push
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(int(op2) + int(op1))

    answer = stack.pop()    # s2에 있는 토큰을 다 사용한 후, 결과적으로 계산된 값 꺼내기

    print(f'#{tc} {answer}')