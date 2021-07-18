# 2021-07-15



## Python 크롤링



1. 작업 및 저장할 디렉토리 내 우클릭 후 Git Bash Here
2. requests 라이브러리, bs4 라이브러리 설치

```bash
pip install requests

pip install beautifulsoup4
```

3. 현재 워킹 디렉토리 우클릭 후 Code(으)로 열기
4. 폴더명 하단에 "새 파일명".py 생성



### 크롤링 예제

>  참고 사이트 `https://api.agify.io?name=michael`
>
>  API 서버는 JSON 타입으로 반환

```python
# 라이브러리 가져오기
import requests

name = 'rosa'

# f'string {변수이름}' 으로 연결
url = f'https://api.agify.io?name={name}'
response = requests.get(url).json()

# print(response) # response로 반환되는 값 확인
print(response['age']) # 'age' key값에 있는 value 출력

```



```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result = exchange.text

print(f'현재 원/달러 환율은 {result}입니다.')

```



```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text # 요청 보내고 받은 응답 text로 변환
data = BeautifulSoup(response, 'html.parser') # 응답으로 받은 걸 처리하기 쉽게 가공(parsing)
kospi = data.select_one('#KOSPI_now')
result = kospi.text

print(f'현재 코스피 지수는{result}입니다.')
```



```python
import requests

name = 'rosa'

# f'string {변수이름}' 형식으로 연결
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()

result = response['country']

for r in result:
    prob = r['probability']
    country = r['country_id']
    print(f'{prob}의 확률로 {country}국적입니다.')
```



### 예제 관련 알게된 점



##### 문자열 내 변수연결

```python
name = 'rosa'

# f'string {변수이름}' 으로 연결
url = f'https://api.agify.io?name={name}'
```

 

##### JSON 타입

```python
# {'key' : 'value'} 쌍으로 이루어진 데이터 타입

url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()

result = response['country']
```

