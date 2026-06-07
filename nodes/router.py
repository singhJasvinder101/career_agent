from schema.state import GraphState
from prompts.router import router_prompt
from schema.route import Route
from nodes.llm import llm

structured_llm = llm.with_structured_output(
    Route
)

def router_node(state: GraphState) -> GraphState:
    last_message = state["messages"][-1].content
    response = structured_llm.invoke(
        router_prompt(last_message, state.get("user_state", {}))
    )
    return {"route": response.destination}