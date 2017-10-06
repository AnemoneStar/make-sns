from flask import jsonify, request, session
from myapp.api.v1 import app
from myapp import models, db
from datetime import datetime

@app.route('/posts')
def postsList():
    posts = models.Post.query.order_by(-models.Post.createdAt).all()
    posts = list(map(lambda x:x.toDict(), posts))
    return jsonify(posts)

@app.route('/posts',methods=["POST"])
def postsCreate():
    post = models.Post()
    post.text = request.form["text"]
    post.userId = session["my_user_id"]
    post.createdAt = datetime.now()
    db.session.add(post)
    db.session.commit()
    return jsonify(post.toDict())