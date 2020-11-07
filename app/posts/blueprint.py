'''
Изолированная функциональность, для которой есть уже шаблоны.
'''
from flask import Blueprint
from flask import render_template

from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
	post = Post.query.all()
	return render_template('posts/index.html', posts=posts)