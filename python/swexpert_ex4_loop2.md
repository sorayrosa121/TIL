# 2021-07-26



## SW Expert Academy 파이썬 프로그래밍 기초(1)



### 흐름과 제어 - 반복 7

```python
grades = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
tot = 0
while grades:
    now = grades.pop()
    if now >= 80:
        tot += now 

print(tot)
```





### 흐름과 제어 - 반복 8

```python
i = 5
while i > 0:
    print('*' * i)
    i -= 1
```





### 흐름과 제어 - 반복 9

```python
i = 7
j = 0
while i > 0:
    print(' '* j + '*' * i + ' '* j)
    i -= 2
    j += 1
```





### 흐름과 제어 - 반복 10

```python
num_dic = dict.fromkeys([str(x) for x in range(10)], 0)
number = int(input())

for j in str(number):
    num_dic[j] += 1

print(*num_dic.keys())
print(*num_dic.values())
```





### 흐름과 제어 - 반복 11

```python
for i in range(1, 5+1):
    print(' ' * (5-i) + '*' * i)
```





### 흐름과 제어 - 반복 13

```python
i = int(input())
answer = ''
while i >= 1:
    a, b = divmod(i, 2)
    answer += str(b)
    i = a

print(answer[::-1])
```
