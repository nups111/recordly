
class Config(object):
    DEBUG = False
    TESTING = False
    API_VERSION = 0

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/recordly_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    DEBUG = True
    LIVESERVER_PORT = 3000
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/recordly_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True