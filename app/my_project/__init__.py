from flask import Flask
from app.my_project.route.routes_blueprint import routes_bp


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    app.register_blueprint(routes_bp)
    return app
