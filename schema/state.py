from langgraph.graph import MessagesState

class GraphState(MessagesState):
    user_state: dict
    plan: dict
    route: str