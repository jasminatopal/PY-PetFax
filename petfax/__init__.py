from flask import Flask 

def create_app(): 
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Topalovic@localhost:5432/pets_fax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        

    from . import models
    from flask_migrate import Migrate
    models.db.init_app(app)    
    Migrate = Migrate(app, models.db) 


# register pet blueprint 
    from . import (pet, fact)
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    return app
