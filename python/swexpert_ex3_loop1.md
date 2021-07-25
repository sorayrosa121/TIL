# 2021-07-25



## SW Expert Academy 파이썬 프로그래밍 기초(1)



### 흐름과 제어 - 반복 1

```python
grades = [88, 30, 61, 55, 95]

for i in range(1, len(grades) +1):
    if grades[i-1] >= 60:
        print(f'{i}번 학생은 {grades[i-1]}점으로 합격입니다.')
    else:
        print(f'{i}번 학생은 {grades[i-1]}점으로 불합격입니다.')
```





### 흐름과 제어 - 반복 2

```python
for i in range(1, 100+1):
    print(i)
```





### 흐름과 제어 - 반복 3

```python
for i in range(1, 100+1):
    if i % 2 == 0:
        print(i, end=" ")
```





### 흐름과 제어 - 반복 4

```python
temp = []
for i in range(1, 100+1, 2):
    temp.append(str(i))

print(', '.join(temp))
```





### 흐름과 제어 - 반복 5

```python
tot = 0
for i in range(1, 100+1):
    if i % 3 == 0:
        tot += i
print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {tot}')
```





### 흐름과 제어 - 반복 6

```python
from collections import Counter

blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
count_type = dict(Counter(blood_type))
print(count_type)
```
