from nodes.router import router_node
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from nodes.memory import memory_retrieve_node
from nodes.memory import memory_update_node
from langchain_core.globals import set_debug, set_verbose
from nodes.planner import planner_node
from schema.state import GraphState
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from dotenv import load_dotenv

set_debug(True)
set_verbose(True)

load_dotenv()

graph = StateGraph(GraphState)

graph.add_node("planner", planner_node)
graph.add_node("memory_update", memory_update_node)
graph.add_node("memory_retrieve", memory_retrieve_node)
graph.add_node("router", router_node)


graph.add_edge(START, "memory_retrieve")
graph.add_edge("memory_retrieve", "router")

graph.add_conditional_edges(
    "router", 
    lambda state: state["route"], 
    {
        "planner": "planner",
        "memory_update": "memory_update",
    }
)

graph.add_edge("planner", "memory_update")
graph.add_edge("memory_update", END)


checkpointer = InMemorySaver()
agent = graph.compile(
    checkpointer=checkpointer
)


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    result = agent.invoke(
        {
            "messages": [ HumanMessage(content=prompt) ]
        },
        {
            "configurable": {
                "thread_id": "user-1"
            }
        }
    )

    print(result)