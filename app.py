from flask import Flask, render_template, request, redirect, url_for
from forms import RegistroForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

posts = []

@app.route('/')
def index():
    return render_template("index.html", num_posts=len(posts))

@app.route('/posts/<string:slug>/')
def show(slug):
    return render_template("detalle.html", slug_title=slug)

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
@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id = None):
    return render_template("admin/post_form.html", post_id=post_id)