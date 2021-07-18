import requests

# naver 요청 보낼 때 필요한 것들
# https://developers.naver.com/apps/#/register 에서 등록 가능

naver_client_id = "네이버 앱 클라이언트 ID"
naver_client_secret = "네이버 앱 클라이언트 SECRET"

# ?query= 추가
URL = "https://openapi.naver.com/v1/search/shop.json?query="

headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret" : naver_client_secret
}

query = "ps5"

product = requests.get(URL + query, headers= headers).json()['items'][0]

product_name = product['title']
product_price = product['lprice']
product_link = product['link']

message = f"{product_name}\n{product_price}\n{product_link}"
print(message)