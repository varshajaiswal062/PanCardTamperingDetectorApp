import os
from   os import environ

class Config(object):

    DEBUG = False
    TESTING = False
    
    basedir    = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'varsha'

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "varsha"

    UPLOADS = "C:/Users/yuvra/Desktop/MSC_Project/Pan Card Tampering Flask App/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "pianalytix"

    UPLOADS = "C:/Users/yuvra/Desktop/MSC_Project/Pan Card Tampering Flask App/app/static/uploads"
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    DEBUG = True

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "pianalytix"

    UPLOADS = "C:/Users/yuvra/Desktop/MSC_Project/Pan Card Tampering Flask App/app/static/uploads"
    SESSION_COOKIE_SECURE = False

 
class DebugConfig(Config):
    DEBUG = False
