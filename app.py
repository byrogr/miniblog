from flask import Flask, render_template, request

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template("index.html", num_posts=len(posts))

@app.route('/posts/<string:slug>/')
def show(slug):
    return render_template("detalle.html", slug_title=slug)

@app.route('/registro/', methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
    return render_template("registro.html")

# Admin
@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id = None):
    return render_template("admin/post_form.html", post_id=post_id)