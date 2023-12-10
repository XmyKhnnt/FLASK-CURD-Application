from flask import Flask
from apps.core.routes import main
from flask_wtf import CSRFProtect

app = Flask(__name__)


app.register_blueprint(main)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'


# Flask-WTF requires this line
csrf = CSRFProtect(app)
if __name__ == '__main__':
    app.run(debug=True)
