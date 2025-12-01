from typing import List, Dict, Any, Optional

from app.my_project.domain.route import Route
from app.my_project.dao import route_dao


def get_all_routes() -> List[Dict[str, Any]]:
    """
    Get all routes as list of JSON-serializable dictionaries.
    """
    routes = route_dao.find_all()
    return [r.__dict__ for r in routes]


def get_route(route_id: int) -> Optional[Dict[str, Any]]:
    """
    Get single route by ID as dictionary.
    """
    route = route_dao.find_by_id(route_id)
    if route is None:
        return None
    return route.__dict__


def create_route(data: Dict[str, Any]) -> int:
    """
    Create new route using raw data from HTTP request body.
    """
    route = Route(
        id=None,
        name=data["name"],
        description=data["description"],
        duration=int(data["duration"]),
        price_per_person=float(data["price_per_person"]),
        route_type_id=int(data["route_type_id"]),
        hotel_id=int(data["hotel_id"]) if data.get("hotel_id") is not None else None,
    )
    return route_dao.create(route)


def update_route(route_id: int, data: Dict[str, Any]) -> bool:
    """
    Update existing route by ID using request data.
    """
    route = Route(
        id=route_id,
        name=data["name"],
        description=data["description"],
        duration=int(data["duration"]),
        price_per_person=float(data["price_per_person"]),
        route_type_id=int(data["route_type_id"]),
        hotel_id=int(data["hotel_id"]) if data.get("hotel_id") is not None else None,
    )
    return route_dao.update(route_id, route)


def delete_route(route_id: int) -> bool:
    """
    Delete route by ID.
    """
    return route_dao.delete(route_id)

def get_route_with_relations(route_id: int) -> Optional[Dict[str, Any]]:
    """
    Get route with its related guides (M:N) and departures (1:N).

    Parameters
    ----------
    route_id : int
        ID of the route.

    Returns
    -------
    dict | None
        Dictionary containing route data with extra keys:
        - "guides": list of guides working on this route
        - "departures": list of tour departures for this route

        None if route does not exist.
    """
    route = route_dao.find_by_id(route_id)
    if route is None:
        return None

    guides = route_dao.find_guides_for_route(route_id)
    departures = route_dao.find_departures_for_route(route_id)

    result: Dict[str, Any] = route.__dict__.copy()
    result["guides"] = guides
    result["departures"] = departures

    return result

def get_route_guides(route_id: int) -> List[Dict[str, Any]]:
    """
    Get list of guides (M:N relation) for a specific route.

    Parameters
    ----------
    route_id : int
        ID of the route.

    Returns
    -------
    List[dict]
        List of guide dictionaries for the given route.
    """
    return route_dao.find_guides_for_route(route_id)


def get_route_departures(route_id: int) -> List[Dict[str, Any]]:
    """
    Get list of tour departures (1:N relation) for a specific route.

    Parameters
    ----------
    route_id : int
        ID of the route.

    Returns
    -------
    List[dict]
        List of departure dictionaries for the given route.
    """
    return route_dao.find_departures_for_route(route_id)
