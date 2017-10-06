from myapp import app, models
import flask

# TODO: あとでこのへんで認証情報をviewに渡したりする←やった
def render_template(*args,**kwargs):
    kwargs["login"] = get_session_account()
    return flask.render_template(*args,**kwargs)

def get_session_account():
    """現在ログインしているアカウントを返す"""
    account = None
    if flask.session.get("my_user_id") != None:
        account = models.User.query.filter_by(id=flask.session["my_user_id"]).first()
    return account
