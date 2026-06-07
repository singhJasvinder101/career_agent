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

graph.add_edge(START, "planner")
graph.add_edge("planner", END)

agent = graph.compile()


if __name__ == "__main__":
    result = agent.invoke({
        "prompt":
        "Become backend engineer in 6 months"
    })

    print(result)