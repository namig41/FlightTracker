import asyncio
import json

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.database import Base, async_session, engine

from app.bookings.models import Bookings
from app.hotels.models import Hotels
from app.users.models import Users
from app.rooms.models import Rooms

from app.main import app as fastapi_app


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all())
        await conn.run_sync(Base.metadata.create_all())

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.csv", "r", encoding="utf-8") as file:
            return json.load(file)

    hotels = open_mock_json("moc_hotels.csv")
    rooms = open_mock_json("moc_rooms.csv")
    users = open_mock_json("moc_users.csv")
    bookings = open_mock_json("moc_bookings.csv")

    async with async_session() as session:
        add_hotels = insert(Hotels).values(hotels)
        add_rooms = insert(Rooms).values(rooms)
        add_users = insert(Users).values(users)
        add_bookings = insert(Bookings).values(bookings)

        await session.execute(add_hotels)
        await session.execute(add_rooms)
        await session.execute(add_users)
        await session.execute(add_bookings)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def session():
    async with async_session() as session:
        yield session
