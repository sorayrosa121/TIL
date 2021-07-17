# 2021-07-16



## 텔레그램 챗봇 API 활용하기 2



### requests 라이브러리



1. 폴더 내 마우스 우클릭 후, "Git Bash Here"로 해당 디렉토리의 Git Bash 열기





2. Git Bash에 "pip install requests" 를 작성하여 requests 라이브러리 설치 (큰 따옴표 표기 안 함)

   ```bash
   pip install requests
   ```

    

   

* ​	requests 라이브러리가 미설치 된 경우

  ```bash
  File "filename.py", line 1, in <module>
      import requests
  ImportError: No module named requests
  ```

 



- requests 라이브러리가 이미 설치된 적 있는 경우

  ```bash
  Requirement already satisfied: requests in "...mypythonpath\lib\site-packages"
  ```





### VSCode로 Python 코드 작성하기



1. requests 라이브러리 가져오기

   

   ```python
   import requests
   ```





2. 기존 저장해둔 챗봇 토큰을 token 변수에, api 사용을 위한 url주소를 app_url 변수에 저장

   

   ```python
   # 기본 설정
   
   # token은 챗봇별로 다르게 나타남
   token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" 
   
   ### string interpolation*을 사용하여 "app_url" 변수의 문자열 안에 "token" 변수의 문자열을 치환
   # app_url = "https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
   app_url = f"https://api.telegram.org/bot{token}"
   
   ```

   > string interpolation* 이란, "문자열 보간"으로도 불리며, **f-strings** (python 3.6이상), **%-formatting**, **Str.format()** 등의 형태로 문자열 속에 다른 문자열의 값을 삽입, 치환해주는 방법

   > [GeeksforGeeks 설명 링크](https://www.geeksforgeeks.org/python-string-interpolation/)





3.  getUpdates로 chat_id 가져오기

    

   ```python
   # updates_url = "https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getUpdates"
   updates_url = f"{app_url}/getUpdates"
   
   response = requests.get(updates_url).json() # getUpdates에서 얻은 값을 json으로 response에 저장
   ```

   

   

4. response을 정제하여 chat_id에 값을 저장

   

   ```python
   # chat_id는 개인 계정별로 다르게 주어짐
   # ex) chat_id = "135791357"
   
   chat_id = response.get("result")[0].get("message").get("chat").get("id")
   ```

   



5. chat_id로 전송할 메시지를 text 변수에 저장

    

   ```python
   text = "Hello World"
   ```

   



6.  sendMessage로 text 메시지 보내기

   ```python
   # message_url = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
   message_url = f"{app_url}/sendMessage?chat_id={chat_id}&text={text}"
   
   requests.get(message_url)
   ```

   

