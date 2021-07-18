import requests

# 기본 설정

# token은 챗봇별로 다르게 나타남
token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" 

### string interpolation*을 사용하여 "app_url" 변수의 문자열 안에 "token" 변수의 문자열을 치환
# app_url = "https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
app_url = f"https://api.telegram.org/bot{token}"

# updates_url = "https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getUpdates"
updates_url = f"{app_url}/getUpdates"

response = requests.get(updates_url).json() # getUpdates에서 얻은 값을 json으로 response에 저장

# chat_id는 개인 계정별로 다르게 주어짐
# ex) chat_id = "135791357"

chat_id = response.get("result")[0].get("message").get("chat").get("id")

text = "Hello World"

# message_url = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
message_url = f"{app_url}/sendMessage?chat_id={chat_id}&text={text}"

requests.get(message_url)