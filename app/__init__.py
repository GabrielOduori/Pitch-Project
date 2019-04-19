from flask_sqlalchemy import SQLAlchemy 

def create_app(config_name):
    app = Flask(__name__)
    
    
    
    
    # Initilaizing flask extensions
    
    db.init_app(app)