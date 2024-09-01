from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # UPLOAD_FOLDER = 'uploads'
    # ARTICLES_FOLDER = 'articles'

    # os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    # os.makedirs(ARTICLES_FOLDER, exist_ok=True)

    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # app.config['ARTICLES_FOLDER'] = ARTICLES_FOLDER

    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
    app.config['ARTICLES_FOLDER'] = os.path.join(app.root_path, 'articles')

    from .routes import setup_routes
    setup_routes(app)

    return app