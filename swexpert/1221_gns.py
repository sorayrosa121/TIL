str_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
num_match = {}  # {string 형태 : 0~9까지 숫자}
for idx, s_num in enumerate(str_numbers):
    num_match[
        s_num] = idx  # {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for _ in range(T):
    cnt_dict = {}  # {arr에 나열된 string형태 : 해당 값 count}
    for i in range(10):
        cnt_dict[i] = 0

    tc, N = input().split()
    N = int(N)  # str타입 int로 변경

    arr = list(input().split())
    for x in arr:
        cnt_dict[num_match[x]] += 1

    print(tc)
    for key, value in cnt_dict.items():
        for i in range(value):
            print(str_numbers[key], end=' ')
    print()