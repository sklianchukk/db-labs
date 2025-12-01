from typing import List, Optional, Dict, Any

from app.my_project.dao.db import get_connection
from app.my_project.domain.route import Route


def _row_to_route(row: Dict[str, Any]) -> Route:
    """
    Convert dictionary row returned from cursor to Route DTO.
    """
    return Route(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        duration=row["duration"],
        price_per_person=float(row["price_per_person"]),
        route_type_id=row["route_type_id"],
        hotel_id=row["hotel_id"],
    )


def find_all() -> List[Route]:
    """
    Fetch all routes from the database.
    """
    query = """
        SELECT id, name, description, duration,
               price_per_person, route_type_id, hotel_id
        FROM routes
        ORDER BY id;
    """

    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        rows = cursor.fetchall()
        return [_row_to_route(row) for row in rows]
    finally:
        cursor.close()
        conn.close()


def find_by_id(route_id: int) -> Optional[Route]:
    """
    Fetch a single route by its ID.
    """
    query = """
        SELECT id, name, description, duration,
               price_per_person, route_type_id, hotel_id
        FROM routes
        WHERE id = %s;
    """

    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (route_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return _row_to_route(row)
    finally:
        cursor.close()
        conn.close()


def create(route: Route) -> int:
    """
    Insert a new route and return the new ID.
    """
    query = """
        INSERT INTO routes
            (name, description, duration, price_per_person, route_type_id, hotel_id)
        VALUES (%s, %s, %s, %s, %s, %s);
    """

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            query,
            (
                route.name,
                route.description,
                route.duration,
                route.price_per_person,
                route.route_type_id,
                route.hotel_id,
            ),
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()


def update(route_id: int, route: Route) -> bool:
    """
    Update existing route.

    Returns
    -------
    bool
        True if any row was updated, False otherwise.
    """
    query = """
        UPDATE routes
        SET name = %s,
            description = %s,
            duration = %s,
            price_per_person = %s,
            route_type_id = %s,
            hotel_id = %s
        WHERE id = %s;
    """

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            query,
            (
                route.name,
                route.description,
                route.duration,
                route.price_per_person,
                route.route_type_id,
                route.hotel_id,
                route_id,
            ),
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()


def delete(route_id: int) -> bool:
    """
    Delete route by ID.

    Returns
    -------
    bool
        True if any row was deleted, False otherwise.
    """
    query = "DELETE FROM routes WHERE id = %s;"

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (route_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()

def find_guides_for_route(route_id: int) -> List[Dict[str, Any]]:
    """
    Fetch guides assigned to a specific route (M:N relation via route_guides).

    Parameters
    ----------
    route_id : int
        ID of the route for which guides should be fetched.

    Returns
    -------
    List[dict]
        List of dictionaries with guide and assignment information.
        Each dict contains keys: id, first_name, last_name, start_date, end_date.
    """
    query = """
        SELECT
            g.id,
            g.first_name,
            g.last_name,
            rg.start_date,
            rg.end_date
        FROM route_guides rg
        JOIN guides g ON g.id = rg.guide_id
        WHERE rg.route_id = %s
        ORDER BY g.last_name, g.first_name;
    """

    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (route_id,))
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        conn.close()


def find_departures_for_route(route_id: int) -> List[Dict[str, Any]]:
    """
    Fetch tour departures (1:N relation) for a specific route.

    Parameters
    ----------
    route_id : int
        ID of the route.

    Returns
    -------
    List[dict]
        List of dictionaries with departure information.
        Each dict contains keys: id, start_date, status, price_per_person.
    """
    query = """
        SELECT
            id,
            start_date,
            status,
            price_per_person
        FROM tour_departures
        WHERE route_id = %s
        ORDER BY start_date;
    """

    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (route_id,))
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        conn.close()