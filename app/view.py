'''
Model - db (модель базы данных)
View - отображение данных
Controller - отвечает за получение, обработку и перенаправление ответа
В Джанго view это контролер.
'''
from app import app
from flask import render_template
'''
декоратор хранит в себе словарь {'url': 'index'}

А ниже это будет {'/': 'index'}
index это ссылка на модуль, которая будет обрабатываться.
Ниже это обёртки, которые ведут по адресам. А под ними должны
быть функции, которые сработают для обработки....
@app.route('/')
@app.route('/blog')
def index():
	return "Hello world"
Выше команда будет записана в словаре как {'/blog': 'index'}
т.е. по адресу /blog вызови метод index.
'''
@app.route('/')
def index():
	name = 'Ivan'
	return render_template('index.html', n=name)
