from langgraph.store.memory import InMemoryStore
from nodes.router import router_node
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from nodes.memory import memory_retrieve_node
from nodes.memory import memory_update_node
from langchain_core.globals import set_debug, set_verbose
from nodes.planner import planner_node
from nodes.chat import chat_node
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
graph.add_node("chat", chat_node)


graph.add_edge(START, "memory_retrieve")
graph.add_edge("memory_retrieve", "router")

graph.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "planner": "planner",
        "memory_update": "memory_update",
        "chat": "chat",
    },
)

graph.add_edge("planner", "memory_update")
graph.add_edge("memory_update", "chat")
graph.add_edge("chat", END)


checkpointer = InMemorySaver()
store = InMemoryStore()

agent = graph.compile(
    checkpointer=checkpointer,
    store=store
)


if __name__ == "__main__":
    while True:
        print("Enter 'exit' to end the conversation")
        prompt = input("Enter your prompt: ")
        if prompt == "exit":
            break

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

        print(result["messages"][-1].content)