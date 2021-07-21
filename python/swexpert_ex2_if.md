# 2021-07-21



## SW Expert Academy 파이썬 프로그래밍 기초(1)



### 흐름과 제어 - If 1

```python
n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(f"{i}(은)는 {n}의 약수입니다.")
```





### 흐름과 제어 - If 2

```python
n = int(input())
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        print(f"{i}(은)는 {n}의 약수입니다.")
        cnt +=1
if cnt <= 2:
    print(f"{n}(은)는 1과 {n}로만 나눌 수 있는 소수입니다.")
```





### 흐름과 제어 - If 3

```python
letter = input()

if letter.lower() == letter:
	print(f"{letter} 는 소문자 입니다.")
else:
    print(f"{letter} 는 대문자 입니다.")
```





### 흐름과 제어 - If 4

```python
man1 = input()
man2 = input()

if man1 == man2:
	print("Result : Draw")

else:
    if man1 == "바위" and man2 == "가위":
        print("Result : Man1 Win!")
    elif man1 == "바위" and man2 == "보":
        print("Result : Man2 Win!")
    elif man1 == "가위" and man2 == "보":
        print("Result : Man1 Win!")
    elif man1 == "가위" and man2 == "바위":
        print("Result : Man2 Win!")
```





### 흐름과 제어 - If 5

```python
letter = input()

if letter.islower():
    print(f"{letter}(ASCII: {ord(letter)}) => {letter.upper()}(ASCII: {ord(letter.upper())})")

elif letter.isupper():
    print(f"{letter}(ASCII: {ord(letter)}) => {letter.lower()}(ASCII: {ord(letter.lower())})")

else:
    print(letter)
```





### 흐름과 제어 - If 7

```python
seven = []

for i in range(1, 200+1):
    if i % 7 == 0 and i % 5 != 0:
        seven.append(i)
    
seven_str = [str(x) for x in seven]

print(",".join(seven_str))
```





### 흐름과 제어 - If 8

```python
even = []

for i in range(100, 300+1):
    s = str(i)
    if int(s[0]) % 2 == 0:
        if int(s[1]) % 2 == 0:
            if int(s[2]) % 2 == 0:
                even.append(s)

print(",".join(even))
```

