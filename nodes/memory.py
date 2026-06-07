from schema.schema import UpdateMemory
from prompts.memory import memory_prompt
from memory import MEMORY
from schema.state import GraphState
from nodes.llm import llm

structured_llm = llm.with_structured_output(UpdateMemory)


def memory_update_node(state: GraphState) -> GraphState:
    prompt = memory_prompt(state["messages"][-1]["content"])
    response = structured_llm.invoke(prompt)
    if response.should_update:
        MEMORY[response.key] = response.value
    return {"user_state": MEMORY}

def memory_retrieve_node(state: GraphState) -> GraphState:
    return {"user_state": MEMORY}