from flask import Flask

app = Flask(__name__)
name = "游莧菖"
id = "B11106042"



@app.route('/')
def rootpage():
    return "<h1>Welcome my website"

@app.route('/who')
def hello():
    return f'<h1>姓名：{name}<br> 學號：{id}</h1>'

@app.route('/home')
def home():
    return '<h1>It is my home</h1>'

@app.route('/about')
def about():
    return '<h1>I do not know</h1>'


if __name__ == '__main__':
    app.run()