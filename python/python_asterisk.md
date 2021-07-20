# 2021-07-20



## Python asterisk 사용법



#### Q. 자연수 number를 입력 받은 후, 1부터 number까지 증가하며, 높이 number만큼 한줄씩 출력하기

```
[입력 예시]
5

[출력 예시]
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```





#### A.1 Asterisk 사용

```python
number = int(input())
tmp = []

for i in range(1, number+1):
    tmp.append(i)
    print(*tmp)

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
```



#### A.2 for문으로 출력

```python
number = int(input())
tmp = []

for num in range(1, number+1):
    tmp.append(num)
    for i in tmp:
        print(i, end = " ")
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
```

