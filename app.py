from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rafadb@localhost/postgres'

app.debug=True
db = SQLAlchemy(app)
db.init_app(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)

    def __init__(self,username,email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    users = User.query.all()
    one_user = User.query.filter_by(username="Rafa").first()
    return render_template('index.html', users=users, one_user=one_user)

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('profile.html', user=user)

@app.route('/post_user', methods=['POST'])
def post_user():
    if request.method == "POST":
        user = User(request.form['username'], request.form['email'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()