from api import app
from flask import render_template


if __name__=="__main__":
    app.run(debug=app.config['DEBUG'])
