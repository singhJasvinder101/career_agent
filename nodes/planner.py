from schema.state import GraphState
from prompts.planner import planner_prompt
from schema.schema import Plan
from nodes.llm import llm

structured_llm = llm.with_structured_output(Plan)

def planner_node(state: GraphState) -> GraphState:
    prompt = planner_prompt(state["prompt"], state["user_state"])

    response = structured_llm.invoke(prompt)
    return {"plan": response}