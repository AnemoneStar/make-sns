from flask import Blueprint
app = Blueprint(__name__,"api_v1",url_prefix="/api/v1")

import myapp.api.v1.posts