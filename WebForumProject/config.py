class Config(object):
    SECRET_KEY = 'IhrGeheimerSchlüssel'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost:3307/webforum'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

