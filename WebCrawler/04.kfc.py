# KEY:肯德基餐厅信息爬取
import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
city = input('enter a city:')
all_city_info = []
for page in range(1, 7):
    page = str(page)
    data = {
        'cname': '',
        'pid': '',
        'keyword': city,
        'pageIndex': page,
        'pageSize': '10',
    }
    response = requests.post(url=post_url, data=data, headers=headers).json()
    all_city_info.append(response)
filename = city+'.json'
fp = open(filename, 'w', encoding='utf-8')
json.dump(all_city_info, fp=fp, ensure_ascii=False)
print('over!!')
