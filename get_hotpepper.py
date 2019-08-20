import requests
import json

def get_hotpepper_data(address):
    url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=42d7b837037c7438&format=json&order=4&count=10&'
    response = requests.get(url)
    shop_url = url + 'address='+address
    response = requests.get(shop_url)
    shop_data = json.loads(response.text) #dct型に変換
    shop_results = shop_data['results']
    mises = shop_results['shop'] #list
    mise_list = []
    for mise in mises:
        shop_name = mise['name']
        mise_list.append(shop_name)
        # print(mise_list)
    return {'stores': mise_list}
