# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS


# app = Flask(__name__)
# CORS(app)

# app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///mydatabase.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for your frontend host
CORS(app, resources={r"/*": {"origins": "https://crud-flask-xwmq.onrender.com"}})

# Database Configuration (You can change this to match your deployed database URL)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"  # Or any remote DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Secret key for session handling or other needs
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "your_default_secret_key")

# Set your database
db = SQLAlchemy(app)

if __name__ == "__main__":
    # Run Flask with the appropriate host and port for Render deployment
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)), debug=True)


