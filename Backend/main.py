from flask import Flask
from flask import render_template, request, redirect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
import pytz

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
JST = pytz.timezone('Asia/Tokyo')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///doggo15.db"
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=lambda: datetime.now(JST))
    username: Mapped[str] = mapped_column(db.String(20),unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(20),unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/LoginPage")
def LoginPage():
    return render_template('LoginPage.html')

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        tittle = request.form.get("title")
        tittle = request.form.get("title")
        post = Post(title=title, body=body)

        db.session.add(post)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('create.html')
