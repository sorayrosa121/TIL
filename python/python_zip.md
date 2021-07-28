## zip() 관련 궁금증

### Q1) zip(a, b) 에서 a와 b의 길이가 다를 때 

#### 짧은 길이(ex. boys)를 가진 리스트 갯수까지만 출력

-   case 1) a, b 길이가 같을 때

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']

print(list(zip(girls, boys)))

# [출력] 
# [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```

- case 2) a, b 길이가 다를 때

```python
girls = ['jane', 'ashley', 'mary', 'sarah', 'britney']
boys = ['justin', 'eric', 'david']

print(list(zip(girls, boys)))

# [출력] 
# [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```

### Q2) zip(set_a, set_b)의 묶이는 순서

### set는 순서가 없으므로 zip(a, b)의 출력 결과에서도 순서없이 묶이는 것을 확인

```python
a = {2, 7, 3}
b = {'d', 'b', 'c'}

print(list(zip(a, b)))

# [출력]
# [(2, 'd'), (3, 'b'), (7, 'c')]
```