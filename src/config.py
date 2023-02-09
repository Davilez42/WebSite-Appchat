class Config:
    SECRET_KEY = 'bro86662'


class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'appchat'


config ={
    'development':DevelopmentConfig
}