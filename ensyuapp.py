# import の実行
from flask import Flask,jsonify
from get_weather import get_weather_data
from get_hotpepper import get_hotpepper_data

# インスタンスの作成
ensyuapp = Flask(__name__)
ensyuapp.config['JSON_AS_ASCII'] = False

# URL, Methodと関数の紐づけ
@ensyuapp.route('/ensyu')
def home():

    weather_data = get_weather_data()
    hotpper_data = get_hotpepper_data('浅草橋')
    
    response = {
        'weather_data': weather_data,
        'hotpper_data': hotpper_data
    }
    
    return jsonify(response)

# サーバの起動
ensyuapp.run(host='0.0.0.0', port=80)