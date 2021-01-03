# KEY: 百度翻译爬取
import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
post_url = 'https://fanyi.baidu.com/sug'
word = input('enter a word:')
data = {
    'kw': word
}
response = requests.post(url=post_url, data=data, headers=headers)
dic_obj = response.json()
filename = word+'.json'
fp = open(filename, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)
print('over!!')
