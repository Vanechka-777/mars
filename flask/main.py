from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def glav():
    return "Миссия Колонизация Марса"


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        return render_template('prof_engineer.html', prof=prof)
    else:
        return render_template('prof_scientist.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')