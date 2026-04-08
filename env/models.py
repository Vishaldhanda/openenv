from pydantic import BaseModel
from typing import List, Optional

class Email(BaseModel):
    id: int
    subject: str
    body: str
    sender: str

class Observation(BaseModel):
    inbox: List[Email]
    current_email: Optional[Email]
    time_step: int

class Action(BaseModel):
    action_type: str  # classify / reply / delete / skip
    label: Optional[str] = None  # urgent / normal / spam
    response: Optional[str] = None

class Reward(BaseModel):
    score: float
    reason: str