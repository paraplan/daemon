from datetime import date
from typing import Any

from aiohttp import ClientSession

from src.env import DATABASE_URL, PARSER_URL


async def _get(url: str, params: dict) -> bytes:
    async with ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.read()


async def _put(url: str, data: Any) -> str:
    async with ClientSession() as session:
        async with session.put(url, json=data) as response:
            return await response.text()


async def put_hour(
    occupation: str,
    number: int,
    sub_group: int,
    cabinet_number: str | None = None,
    cabinet_details: str | None = None,
) -> str:
    return await _put(DATABASE_URL + "/hour", data=locals())


async def put_study_day(
    group_full_name: str, group_name: str, hour_ids: list[str], date: str
) -> str:
    return await _put(DATABASE_URL + "/study_day", data=locals())


async def get_schema(date: date) -> bytes:
    return await _get(PARSER_URL + "/study_day", {"date": date.isoformat()})
