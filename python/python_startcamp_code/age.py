import requests

name = 'rosa'

# f'string {변수이름}' 으로 연결
url = f'https://api.agify.io?name={name}'
response = requests.get(url).json()

print(response)
print(response['age']) # 'age' key값에 있는 value 출력
