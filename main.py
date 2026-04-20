from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def glav():
    return "Миссия Колонизация Марса"


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
        return render_template('training.html', prof=prof)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    return render_template('list_prof.html', list_type=list_type)

@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    context = {
        'title': 'Анкета кандидата',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'пилот марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **context)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')