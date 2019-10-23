from flask import Flask

app = Flask(__name__)
# 初始化Flask这个类
# __name__ 是import_name, Flask 会更具这个name获取到当前路径


@app.route("/")
def index():
    return "hello world"


app.run()
