from flask import Flask
from database.db import init_db
from auth.jwt_handler import jwt

from routes.auth_routes import auth_bp
from routes.book_routes import book_bp
from routes.borrow_routes import borrow_bp

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(book_bp, url_prefix="/books")
app.register_blueprint(borrow_bp, url_prefix="/borrow")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)