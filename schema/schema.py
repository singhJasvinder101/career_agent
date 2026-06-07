from pydantic import BaseModel

class Plan(BaseModel):
    goal: str
    steps: list[str]

class UpdateMemory(BaseModel):
    should_update: bool
    key: str
    value: str