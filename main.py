from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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