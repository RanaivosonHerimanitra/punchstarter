#where you declared your database:
import os
DEBUG=True
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI="sqlite:///" + BASE_DIR + "/app.db"