from schema.schema import Plan
from typing import TypedDict

class GraphState(TypedDict):
    prompt: str
    user_state: dict
    plan: Plan
