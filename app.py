from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, current_user
from werkzeug.urls import url_parse

from forms import RegistroForm, PostForm, LoginForm
from models import users

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

loginManager = LoginManager(app)

posts = []

@loginManager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/')
def index():
    return render_template("index.html", posts=posts)

@app.route('/posts/<string:slug>/')
def show(slug):
    return render_template("detalle.html", slug_title=slug)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    # if form.validate_on_submit():
        #
    
    return render_template('login.html', form=form)

@app.route('/registro/', methods=["GET", "POST"])
def registro():
    formRegistro = RegistroForm()
    if formRegistro.validate_on_submit():
        name = formRegistro.name.data
        email = formRegistro.email.data
        password = formRegistro.password.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return url_for('index')
    return render_template("registro.html", form=formRegistro)

# Admin
@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
def post_form(post_id):
    postForm = PostForm()
    if postForm.validate_on_submit():
        title = postForm.title.data
        slug = postForm.slug.data
        content = postForm.content.data

        post = {'title': title, 'slug': slug, 'content': content}
        posts.append(post)

        return redirect(url_for('index'))
    return render_template("admin/post_form.html", form=postForm)