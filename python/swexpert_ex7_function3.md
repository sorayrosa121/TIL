# 2021-08-03



## SW Expert Academy 파이썬 프로그래밍 기초(1)



### 함수의 기초 7

```python
n = int(input())

def fact(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    
    return answer

print(fact(n))
```





### 함수의 기초 8

```python
def square(n):
    answer = n ** 2
    return f'square({n}) => {answer}'

def multi(num):
    for n in num:
        print(square(n))
    
data = list(map(int, input().split(',')))

multi(data)
```





### 함수의 기초 9

```python
def longer(a, b):
    if len(a) >= len(b):
        return a
    return b

x, y = input().split(', ')

print(longer(x, y))
```





### 함수의 기초 10

```python
def countdown(n):
    if n <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    for i in range(n, 0, -1):
        print(i)

countdown(0)
countdown(10)
```