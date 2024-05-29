from pydantic import BaseModel, Field

from src.models.base import BaseItem
from src.models.hours import Hour

LessonType = dict[int, Hour]
SubGroupsType = dict[int, LessonType]


class Group(BaseModel):
    info: BaseItem
    extramural: bool
    course: int
    number: int
    prefix: str
    subgroups_hours: SubGroupsType = Field(validation_alias="hours")
