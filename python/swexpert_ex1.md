# 2021-07-19



## SW Expert Academy 파이썬 프로그래밍 기초1



### 변수

```python
a = int(input())

cnt = 0
for i in range(1, 5):
    cnt += int(str(a) * i)
print(cnt)
```







### 연산자 1

```python
inch = int(input())

print("%.2f inch => %.2f cm " %(inch, inch * 2.54))
```





### 연산자 2

```python
kg = int(input())

print("%.2f kg =>  %.2f lb " %(kg, kg * 2.2046))
```





### 연산자 3

```python
celsius = int(input())

print("%.2f ℃ =>  %.2f ℉ " %(celsius, celsius * (180 / 100) + 32))
```





### 연산자 4

```python
fahrenheit = int(input())

print("%.2f ℉ =>  %.2f ℃" %(fahrenheit, (fahrenheit - 32) * (100 / 180)))
```





### 연산자 5

```python
salt = 0.2 * 100
water = 100 + 200
mixed = salt / water * 100

print("혼합된 소금물의 농도: %.2f%%" %(mixed))
```


