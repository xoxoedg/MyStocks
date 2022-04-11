import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://root:root@localhost:5432/stocks"


class ProdConfig(Config):
    TESTING = False


class DevConfig(Config):
    TESTING = True
