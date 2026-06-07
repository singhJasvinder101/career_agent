from schema.schema import UpdateMemory
from prompts.memory import memory_prompt
from schema.state import GraphState
from nodes.llm import llm

structured_llm = llm.with_structured_output(UpdateMemory)


def memory_update_node(state, config, *, store) -> GraphState:
    user_id = config["configurable"]["thread_id"]

    prompt = memory_prompt(
        state["messages"][-1].content,
        state.get("user_state", {}),
    )

    response = structured_llm.invoke(prompt)
    if response.should_update:
        store.put(("users", user_id), response.key, {"value": response.value})

    memories = store.search(("users", user_id), limit=100)
    user_state = {item.key: item.value["value"] for item in memories}

    return {
        "user_state": user_state,
        "memory_update": {
            "updated": response.should_update,
            "key": response.key if response.should_update else "",
            "value": response.value if response.should_update else "",
        },
    }

def memory_retrieve_node(state, config, *, store) -> GraphState:
    user_id = config["configurable"]["thread_id"]
    
    memories = store.search(("users", user_id), limit=100)
    user_state = {item.key: item.value["value"] for item in memories}

    return {"user_state": user_state}