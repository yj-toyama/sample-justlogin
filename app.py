from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html', title="top page",message="what your name")

@app.route('/',methods=['POST'])
def form():
    field = request.form['field']
    return render_template('index.html',title="logined",message="hello %s-san!!" % field)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')