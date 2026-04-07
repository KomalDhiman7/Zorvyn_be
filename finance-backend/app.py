from flask import Flask
from routes.user_routes import user_bp
from routes.record_routes import record_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(record_bp, url_prefix="/records")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

@app.route("/")
def home():
    return {"message": "Working"}

if __name__ == "__main__":
    app.run(debug=True)