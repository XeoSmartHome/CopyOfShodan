class BaseConfig:
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PASSWORD_SALT = '12345'
