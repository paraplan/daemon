from pydantic import BaseModel


class BaseItem(BaseModel):
    full_name: str
    name: str
    id: int
