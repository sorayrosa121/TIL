[TOC]

# SQL



## 1. SQL Query

<br>

```sql
-- 1) countries 테이블 생성
CREATE TABLE countries(
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER)
;

-- 2) 데이터 입력
INSERT INTO countries VALUES('B203', '2019-12-31', '2020-01-03', 'suite' , 900);
INSERT INTO countries VALUES('1102', '2020-01-04', '2020-01-08', 'suite' , 850);
INSERT INTO countries VALUES('303', '2020-01-01', '2020-01-03', 'deluxe' , 500);
INSERT INTO countries VALUES('807', '2020-01-04', '2020-01-07', 'superior' , 300);


-- 3) 테이블 이름 hotels로 변경
ALTER TABLE countries RENAME TO hotels;

-- 4) 객실 가격 내림차순 정렬, 상위 2개의 room_num과 price 조회
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

-- 5) grade별로 분류된 grade 갯수 내림차순 조회
SELECT grade, COUNT(*) FROM hotels GROUP BY grade ORDER BY COUNT(*) DESC;

-- 6) 객실의 위치가 지하 혹은 등급이 deluxe인 객실 정보 조회
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade='deluxe';

-- 7) 지상층 객실이면서, 2020년 1월 4일에 체크인한 객실의 목록을 price 오름차순으로 조회
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price ASC;
```



## SQL ORM 비교하기

<br>

```
id : integer(pk)
first_name : text
last_name : text
age : integer
country : text
phone : text
balance: integer
```

<br>


1. user 테이블 전체 데이터 조회


   `User.objects.all()`
   <br>

2. id 가 19 인 사림의 age를 조회


   `User.objects.filter(pk=19).values('age')`
   <br>

3. 모든 사람의 age컬럼 조회

   

   `User.objects.values('age')`
   <br>

4. age 가 40 이하인 사림들의 id 와 balance 를 조회


   `User.objects.filter(age__gte=40).values('id', 'balance')`
   <br>

5. last_name 이 '김'이고 balance 가 500 이상인 사람들의 first_name을 조회


   `User.objects.filter(last_name='김', balance__gte=500).values('first_name')`
   <br>

6. first_name 이 '수'로 끝나면서 행정구역이 경기도인 사람들의 balance 를 조회


   `User.objects.filter(first_name__endswith='수', country='경기도').values('balance')`
   <br>

7. balance 가 2000 이상이거나 age 가 40 이하인 사람의 총 인원수


   `User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()`
   <br>

8. phone 앞자리가 010’ 으로 시작하는 사람의 총 인원수


   `User.objects.filter(phone__startswith='010').count()`
   <br>

9. 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정
   

   `User.objects.filter(last_name='김', first_name='옥자').update(country='경기도')`

   <br>

10. 이름이 '백진호'인 사람을 삭제
    

    `User.objects.filter(last_name='백', first_name='진호').delete()`
    <br>

11. balance 를 기준으로 상위 4 명의 first_name, last_name, balance 를 조회


    `User.objects.order_by('-balance')[:4].values('first_name', 'last_name', 'balance')`
    <br>

12. phone 에 '123' 을 포함하고 age 가 30 미만인 정보를 조회


    `User.objects.filter(phone__contains='123', age__lt=30)`
    <br>

13. phone 이 '010' 으로 시작하는 사람들의 행정 구역을 중복 없이 조회


    `User.objects.filter(phone__startswith='010').values('country').distinct()`
    <br>

14. 모든 인원의 평균 age


    `User.objects.aggregate(Avg('age'))`
    <br>

15. 박씨의 평균 balance


    `User.objects.filter(last_name='박').aggregate(Avg('balance'))`
    <br>

16. 경상북도에 사는 사람 중 가장 많은 balance 의 액수


    `User.objects.filter(country='경상북도').aggregate(Max('balance'))`
    <br>

17. 제주특별자치도에 사는 사람 중 balance 가 가장 많은 사람의 first_name


    `User.objects.filter(country='제주특별자치도', balance=User.objects.filter(country='제주특별자치도').aggregate(Max('balance'))['balance__max']).values('first_name')`
    <br>

