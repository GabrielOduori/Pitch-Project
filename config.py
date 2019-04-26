import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://goduori:postgres@localhost/pitchlist'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    
    # Email configuration
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://goduori:postgres@localhost/pitchlist_list'
    
class ProConfig(Config):
    
    '''
    General configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("HEROKU_POSTGRESQL_BRONZE_URL")
    SECRET_KEY=os.environ.get("SECRET_KEY")


class DevConfig(Config):
    '''
    Development configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://goduori:postgres@localhost/pitchlist'
    
    DEBUG  =  True
    
    
    
config_options = {
    'development':DevConfig,
    'production':ProConfig,
    'test':TestConfig
}
    