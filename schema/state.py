from typing import Any

from langgraph.graph import MessagesState


class GraphState(MessagesState):
    user_state: dict
    plan: Any
    route: str
    memory_update: dict