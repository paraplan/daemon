from pydantic import BaseModel

from src.models.base import BaseItem
from src.models.group import Group


class Area(BaseModel):
    info: BaseItem
    color: str
    groups: list[Group]
