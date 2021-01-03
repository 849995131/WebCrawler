# KEY:化妆品企业信息爬取
import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
id_list = []  # 存储企业ID
for p in range(1, 10):
    p = str(p)
    data = {
        'on': 'true',
        'page': p,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }
    json_ids = requests.post(url=post_url, data=data, headers=headers).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
# 获取企业详情数据
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
all_data_list = []  # 存储所有企业详情数据
for id in id_list:
    data = {
        'id': id
    }
    detail_json = requests.post(
        url=post_url, data=data, headers=headers).json()
    all_data_list.append(detail_json)
# 持久化存储
fp = open('./hzp.json', 'w', encoding='utf-8')
json.dump(all_data_list, fp=fp, ensure_ascii=False)
print('over!!')
