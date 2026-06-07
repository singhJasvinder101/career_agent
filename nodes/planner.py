from schema.state import GraphState
from prompts.planner import planner_prompt
from schema.schema import Plan
from nodes.llm import llm

structured_llm = llm.with_structured_output(Plan)

def planner_node(state: GraphState) -> GraphState:
    last_message = state["messages"][-1].content

    response = structured_llm.invoke(
        planner_prompt(
            last_message, 
            state["user_state"]
        )
    )
    return {"plan": response}