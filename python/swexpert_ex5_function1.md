# 2021-07-27



## SW Expert Academy 파이썬 프로그래밍 기초(1)



### 함수의 기초 1

```python
word = input()

def backwards(word):
    return word[::-1]

if backwards(word) == word:
    print(word)
    print('입력하신 단어는 회문(Palindrome)입니다.')
```





### 함수의 기초 2

```python
man1 = input()
man2 = input()
hand1 = input()
hand2 = input()

def game(hand1, hand2):
    if hand1 == hand2:
        print("Result : Draw")

    else:
        if hand1 == "바위" and hand2 == "가위":
            print(f"{hand1}가 이겼습니다!")
        elif hand1 == "바위" and hand2 == "보":
            print(f"{hand2}가 이겼습니다!")
        elif hand1 == "가위" and hand2 == "보":
            print(f"{hand1}가 이겼습니다!")
        elif hand1 == "가위" and hand2 == "바위":
            print(f"{hand2}가 이겼습니다!")

game(hand1, hand2)
```





### 함수의 기초 3

```python
n = int(input())

def is_prime(n):
    cnt = 0
    if n == 1:
        return '소수가 아닙니다.'
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
    if cnt == 0:
        return '소수입니다.'
    
    return '소수가 아닙니다.'


print(is_prime(n))
```