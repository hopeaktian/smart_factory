class Config(object):
        SECRET_KEY = ''

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://USER:PASSWORD@IP:3306/DATABASE_NAME"
