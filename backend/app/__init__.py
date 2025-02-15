from flask import Flask
from config import Config
import logging

# Removes "ERROR:root:" from the start of each error log
logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/', methods=['GET'])
    def api_endpoint():
        return {
            "message": "Hello, World!",
            "status": "success"
        }
    
    return app