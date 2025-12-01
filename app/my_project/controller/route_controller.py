from typing import Any, Dict

from flask import jsonify, request
from app.my_project.service import route_service


def register_route_controllers(bp):
    """
    Register all CRUD endpoints for routes on the given Blueprint.

    Parameters
    ----------
    bp : flask.Blueprint
        Blueprint object to which routes will be attached.
    """

    @bp.get("/")
    def list_routes():
        """
        GET /routes/
        Return list of all routes.
        """
        routes = route_service.get_all_routes()
        return jsonify(routes), 200

    @bp.get("/<int:route_id>")
    def get_route(route_id: int):
        """
        GET /routes/<id>
        Return single route by ID.
        """
        route = route_service.get_route(route_id)
        if route is None:
            return jsonify({"error": "Route not found"}), 404
        return jsonify(route), 200

    @bp.post("/")
    def create_route():
        """
        POST /routes/
        Create new route.
        """
        data: Dict[str, Any] = request.get_json()
        new_id = route_service.create_route(data)
        return jsonify({"id": new_id}), 201

    @bp.put("/<int:route_id>")
    def update_route(route_id: int):
        """
        PUT /routes/<id>
        Update existing route.
        """
        data: Dict[str, Any] = request.get_json()
        updated = route_service.update_route(route_id, data)
        if not updated:
            return jsonify({"error": "Route not found"}), 404
        return jsonify({"status": "updated"}), 200

    @bp.delete("/<int:route_id>")
    def delete_route(route_id: int):
        """
        DELETE /routes/<id>
        Delete route.
        """
        deleted = route_service.delete_route(route_id)
        if not deleted:
            return jsonify({"error": "Route not found"}), 404
        return jsonify({"status": "deleted"}), 200
    
    @bp.get("/<int:route_id>/details")
    def get_route_details(route_id: int):
        """
        GET /routes/<id>/details
        Return route with related guides (M:N) and departures (1:N).

        This endpoint is used to demonstrate multi-table queries:
        - M:N via route_guides (route <-> guide)
        - 1:N via tour_departures (route -> many departures)
        """
        result = route_service.get_route_with_relations(route_id)
        if result is None:
            return jsonify({"error": "Route not found"}), 404
        return jsonify(result), 200
    
    @bp.get("/<int:route_id>/guides")
    def get_route_guides(route_id: int):
        """
        GET /routes/<id>/guides
        Return all guides assigned to this route (M:N relation).

        This endpoint demonstrates reading data from the junction table
        route_guides and the guides table.
        """
        guides = route_service.get_route_guides(route_id)
        return jsonify(guides), 200


    @bp.get("/<int:route_id>/departures")
    def get_route_departures(route_id: int):
        """
        GET /routes/<id>/departures
        Return all tour departures for this route (1:N relation).

        This endpoint demonstrates a typical 1:N relation
        (one route -> many departures).
        """
        departures = route_service.get_route_departures(route_id)
        return jsonify(departures), 200


