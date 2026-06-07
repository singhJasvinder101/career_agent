from typing import Literal

from pydantic import BaseModel


class Route(BaseModel):
    destination: Literal["planner", "memory_update"]