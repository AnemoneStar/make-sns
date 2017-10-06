import bcrypt
from myapp import app, models, db
from myapp.utils import render_template
from flask import request, session, redirect
from datetime import datetime
import myapp.config

@app.route('/')
def indexPage():
    return render_template("index.jade",posts=models.Post.query.order_by(-models.Post.createdAt).all())

@app.route('/register')
def registerPage():
    return render_template("register.jade")
@app.route('/register',methods=["POST"])
def registerPostPage():
    user = models.User()
    user.name = request.form["name"]
    user.screenName = request.form["screenName"]
    user.password = bcrypt.hashpw(request.form["password"].encode("UTF-8"),bcrypt.gensalt(myapp.config.BCRYPT_SALT_COUNT))
    user.createdAt = datetime.now()
    user.updatedAt = datetime.now()
    db.session.add(user)
    db.session.commit()
    return str(user.id)

@app.route('/login')
def loginPage():
    return render_template("login.jade")
@app.route('/login',methods=["POST"])
def loginPostPage():
    user = models.User.query.filter_by(screenName=request.form["screenName"]).first()
    if not bcrypt.checkpw(request.form["password"].encode("UTF-8"),user.password.encode("UTF-8")):
        return "invalid password"
    session["my_user_id"] = user.id
    return redirect("/")

@app.route('/logout')
def logoutPage():
    del session["my_user_id"]
    return redirect("/")