# 2021-08-02



## SW Expert Academy 파이썬 프로그래밍 기초(1)



### 함수의 기초 4

```python
n = int(input())
def fib(n):
    answer = [i for i in range(n)]
    for i in range(n):
        if i <= 1:
            answer[i] = 1
        else:
            answer[i] = answer[i-1] + answer[i-2]
    return answer

print(fib(n))
```





### 함수의 기초 5

```python
data = [1, 2, 3, 4, 3, 2, 1]

def dup(data):
    answer = list(set(data))
    return answer

print(data)
print(dup(data))
```





### 함수의 기초 6

- 처음 시도했던 방법:
Pass는 되지만, string 특성으로 인해, 테스트케이스에 따라 오답 가능성이 있다(ex. findn(data, 1)) #=> True

```python
data = [2, 4, 6, 8, 10]

def findn(data, n):
    new_data = [str(x) for x in data]
    new_data = ','.join(new_data)
    if new_data.find(str(n)) == -1:
        return f'{n} => False'
    return f'{n} => True'

print(data)    
print(findn(data, 5))
print(findn(data, 10))
```

- 수정한 답안

```python
data = [2, 4, 6, 8, 10]

def findn(data, n):
    if n not in data:
        return f'{n} => False'
    return f'{n} => True'

print(data)    
print(findn(data, 5))
print(findn(data, 10))
```