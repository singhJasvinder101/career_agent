from langchain_core.messages import AIMessage

from nodes.llm import llm
from prompts.chat import chat_prompt
from schema.state import GraphState


def chat_node(state: GraphState) -> GraphState:
    last_message = state["messages"][-1].content
    plan = state.get("plan")
    plan_payload = plan.model_dump() if plan is not None and hasattr(plan, "model_dump") else plan

    prompt = chat_prompt(
        message=last_message,
        user_state=state.get("user_state", {}),
        route=state.get("route", "chat"),
        plan=plan_payload,
        memory_update=state.get("memory_update"),
    )

    response = llm.invoke(prompt)
    return {"messages": [AIMessage(content=response.content)]}
