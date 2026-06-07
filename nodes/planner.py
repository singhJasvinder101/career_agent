from dotenv import load_dotenv
from prompts.prompts import planner_prompt
from schema.schema import Plan
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

structured_llm = llm.with_structured_output(Plan)

def planner_node(state: dict) -> dict:
    prompt = planner_prompt(state["prompt"])
    response = structured_llm.invoke(prompt)
    return {"plan": response}