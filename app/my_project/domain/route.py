from dataclasses import dataclass
from typing import Optional


@dataclass
class Route:
    """
    Domain model representing a touristic route.

    This is a simple data-transfer object (DTO) that we will
    use between DAO, service and controller layers.
    """

    id: Optional[int]
    name: str
    description: str
    duration: int
    price_per_person: float
    route_type_id: int
    hotel_id: Optional[int] = None
