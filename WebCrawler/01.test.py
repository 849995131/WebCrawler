import requests
# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
url = 'https://www.sogou.com/web'
kw = input('enter a word:')
param = {
    'query': kw
}
response = requests.get(url=url, params=param, headers=headers)
page_text = response.text
filename = kw+'.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(filename, '保存成功!')
