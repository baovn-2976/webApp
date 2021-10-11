from flask import Flask
import os
import socket


from market import app
from flask import render_template
from market.models import Item


#app = Flask(__name__)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug = os.environ.get('DEBUG') == '1')