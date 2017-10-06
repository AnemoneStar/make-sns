from myapp.api.v1 import app as v1_app
from myapp import app

app.register_blueprint(v1_app)