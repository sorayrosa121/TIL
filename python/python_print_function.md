## print(print("hello")) 의 출력 결과 관련 궁금증



### Why?



- (1) print() 작성한 후 출력

```python
print("hello")
print()
print("world")

# hello
# 
# world
```



- (2) 이중으로 print 함수를 작성한 후 출력

```python
print(print("hello"))

# hello
# None
```

> None은 왜 출력되는걸까?



### (1)의 print() 출력결과에 대한 이유!

```python
### 내장함수 print()
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

### (1)의 경우, print("")과 같다면, ""의 타입을 알아보자

print(type(""))
# <class 'str'>
```

> [내장함수 print() 설명 docs](https://docs.python.org/ko/3.6/library/functions.html#print)

- objects없이 print()만 작성하는 경우, end 기본값인 print(end="\n")만 출력되는 것



### (2) 의 print() 속 print("hello")은?

```python
### (2)의 경우를 알아보기위해 print("안녕") 출력 자체의 타입을 확인해보자

type(print("안녕"))
# <class 'NoneType'>
```



### string 타입의 공백 입력 vs. NoneType 입력

```python
### str 타입으로 공백이 입력된 것과 NoneType이 입력된 것은 다르므로...

print("" == None)
# False

print("")
#

print(None)
# None
```



### ∴ print(print("hello")) 의 입력 시 None 출력 

```python
### (1)
print("hello")
print()
print("world")

# hello
# 
# world

### (2)
print(print("hello"))

# hello
# None
```

