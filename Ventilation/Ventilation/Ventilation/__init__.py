"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.debug = True
app.config.from_object('config')
import Ventilation.views
