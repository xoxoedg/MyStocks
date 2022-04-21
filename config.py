import os

basedir = os.path.abspath(os.path.dirname(__file__))


class ProdConfig:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://root:root@localhost:5432/stocks"


class DevConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://root:root@localhost:5432/dev"
