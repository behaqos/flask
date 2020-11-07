from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

#имя текущего файла. Флас от имени отталкиваясь и от его пути будет находить другие файлы
app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)