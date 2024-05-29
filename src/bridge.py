from datetime import date
from uuid import UUID

import orjson
import orjson.orjson
from pydantic import BaseModel

from src.http_client import get_schema, put_hour, put_study_day
from src.models.base import BaseItem
from src.models.group import Group
from src.models.hours import Hour
from src.models.study_day import StudyDay


async def main(date: date):
    study_day_data = await get_schema(date=date)
    # for debug
    # with open("study_day.json", "wb") as f:
    #     f.write(study_day_data)
    # with open("study_day.json", "rb") as f:
    #     study_day_data = f.read()
    study_day = StudyDay(**orjson.loads(study_day_data))
    for area in study_day.areas:
        for group in area.groups:
            group_hours = await get_group_hours(group)
            await add_study_day(
                group_info=group.info,
                hours=group_hours,
                date=study_day.date,
            )


async def get_group_hours(group: Group) -> list[UUID]:
    group_hours: list[UUID] = []
    for hour_number, subgroup in group.subgroups_hours.items():
        for subgroup_number, hour in subgroup.items():
            hour = await add_hour(subgroup_number, hour, hour_number)
            if hour:
                group_hours.append(hour.id)
    return group_hours


class AddHourResponse(BaseModel):
    id: UUID


async def add_hour(subgroup_number: int, hour: Hour, number: int) -> AddHourResponse | None:
    cabinet_number = hour.room.name if hour.room else None
    cabinet_details = hour.room.full_name if hour.room else None
    result = await put_hour(
        occupation=hour.occupation,
        sub_group=subgroup_number,
        number=number,
        cabinet_number=cabinet_number,
        cabinet_details=cabinet_details,
    )
    return AddHourResponse(**orjson.loads(result))


async def add_study_day(group_info: BaseItem, hours: list[UUID], date: date):
    return await put_study_day(
        group_full_name=group_info.full_name,
        group_name=group_info.name,
        hour_ids=list(map(str, hours)),
        date=date.isoformat(),
    )
