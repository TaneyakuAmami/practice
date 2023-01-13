import requests
from fake_useragent import UserAgent

#url = 'https://news.yahoo.co.jp/'
url = 'https://www.google.com/search'
ua = UserAgent()
header = {'user-agent':ua.chrome}
param = {'q':'python'}
response = requests.get(url, headers=header, params=param, timeout=3)

#print(response.text[:500])
for key,value in response.headers.items():
 print(key,'   ',value)
