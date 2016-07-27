import os
basedir = os.path.abspath(os.path.dirname(__file__))


# mail = Mail()

# app = Flask(__name__)
# mail.init_app(app)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    MAIL_SERVER = 'email-smtp.us-east-1.amazonaws.com'
    MAIL_USERNAME = 'AKIAI3HES27X3MSXQZEA'
    MAIL_PASSWORD = 'AuQQ/mTon4kIKEYl+fkow6IMC68bI7XqxgHr6nk5cVdV'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SENDER = "Women's Activism <sgong@records.nyc.gov>"
    # MAIL_RECEIVER = "<sgong9570@gmail.com>"
    MAIL_ADMIN = "<sgong9570@gmail.com>"

    RECAPTCHA_PUBLIC_KEY = '6LeaCCYTAAAAAEQgFc258VCfPgu5iLJZb42JBuZ8'
    RECAPTCHA_PRIVATE_KEY = '6LeaCCYTAAAAAApdJTNppVwy7juVd6ucrcA4wsbn'

    @staticmethod
    def init_app(app):
        pass



    # mail.init_app(app)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
 #   SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
   #     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
  #  SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
 #       'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    pass
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
  #      'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}