# import の実行
from flask import Flask,jsonify,request

# インスタンスの作成
app = Flask(__name__)
programs =[{'title':'aaa'}]

# URL, Methodと関数の紐づけ
@app.route('/programs',methods=['GET'])
def get_programs():
    return jsonify(programs)
    
# @app.route('/program/<name>',methods=['GET'])
# def get_program():
#     return jsonify(program)
    

#サーバの起動
app.run(host='0.0.0.0', port=80, debug=True)