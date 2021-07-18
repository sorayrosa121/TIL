import requests

name = 'rosa'

# f'string {변수이름}' 으로 연결
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()

result = response['country']

for r in result:
    prob = r['probability']
    country = r['country_id']
    print(f'{prob}의 확률로 {country}국적입니다.')