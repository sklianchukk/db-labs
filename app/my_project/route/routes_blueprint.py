from flask import Blueprint
from app.my_project.controller.route_controller import register_route_controllers

routes_bp = Blueprint("routes", __name__, url_prefix="/routes")

# Attach all controller functions to this blueprint
register_route_controllers(routes_bp)
