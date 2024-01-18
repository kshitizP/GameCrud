import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/game_db2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_recycle' : 280}
