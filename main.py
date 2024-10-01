from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///newflask.db"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route("/statya",methods=["POST", "GET"])
def statya():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        post = Post(title=title, text=text)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"Ошибка при добавлении статьи: {e}")
            return "Ошибка при добавлении"
    else:
        return render_template("statya.html")


@app.route("/aut")
def aut():
    return render_template("avtorizacia.html")


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post = post)

@app.route("/avtor")
def avtor():
    return render_template("avtor.html")

@app.route("/")
def main_page():
    try:
        posts = Post.query.all()
        return render_template("index.html",posts=posts)
    except:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()