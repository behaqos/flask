from app import app
from app import db

from posts.blueprint import posts

import view



#создаём точку входа
# if it's main file, launching app via app.run()
'''
Как запустить код с окружением через Sublime?


Постоянно запускаем через main.py

Как включить режим дебага?
	app.run(debug=True), чтобы после изменений сам
	автоматом обновлялся.

'''

app.register_blueprint(posts, url_prefix='/blog')



if __name__ == '__main__':
	app.run()
