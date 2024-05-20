import os
import secrets

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from db import db
import models

from resources.item import blp as ItemBlueprint 
from resources.store import blp as StoreBlueprint 
from resources.tag import blp as TagBlueprint 
from resources.user import blp as UserBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/5.17.10/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)
    
    app.config["JWT_SECRET_KEY"] = "jose"
    jwt = JWTManager(app)
        
    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    
    return app