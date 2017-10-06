import os
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", 'mysql+pymysql://root:@localhost/make-sns')
SECRET_KEY="abc"
BCRYPT_SALT_COUNT=12