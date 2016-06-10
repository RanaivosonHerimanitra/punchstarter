#where you declared your database:
import os
import cloudinary
#import cloudinary.uploader
#import cloudinary.api
DEBUG=True
BASE_DIR= os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI="sqlite:///" + BASE_DIR + "/app.db"
cloudinary.config(cloud_name = "dp47drhss",api_key = "618837768465535",api_secret = "upl9dCfrHhObxyLApgz9ZCakwI0")
