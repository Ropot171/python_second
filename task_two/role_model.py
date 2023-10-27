from pydantic import BaseModel


class Role(BaseModel):
    name: str
    id: int
    description: str