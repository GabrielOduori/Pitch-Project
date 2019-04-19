class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://goduori:postgres@localhost/pitchlist'
    




class ProConfig(Config):
    
    '''
    General configuration child class
    '''
    
    pass



class DevConfig(Config):
    '''
    Development configuration child class
    '''
    
    DEBUG  =  True
    
    
    
config_options = {
    'development':DevConfig,
    'production':ProConfig
}
    