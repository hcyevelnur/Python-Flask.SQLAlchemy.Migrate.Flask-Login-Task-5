from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@127.0.0.1:3308/task_flask"
app.config['SECRET_KEY'] = 'any secret string'

SQLALCHEMY_TRACK_MODIFICATIONS = True


from extensions import *
from controllers import *
from models import *


if __name__ == '__main__':
    db.init_app(db)
    db.init_app(migrate)
    app.run(port=5000, debug=True)