from flask import Flask

app = Flask(__name__)

from deliberate_spending import views
