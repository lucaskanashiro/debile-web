from flask import Flask
from debuild.blueprints.api import api
from debuild.blueprints.site import site

app = Flask(__name__)
app.register_blueprint(site)
app.register_blueprint(api, url_prefix='/api')


app.run(debug=True)