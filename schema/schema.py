from pydantic import BaseModel

class Plan(BaseModel):
    goal: str
    steps: list[str]