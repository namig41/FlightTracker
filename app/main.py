from fastapi import FastAPI, Query, Depends

from app.admin.auth import authentication_backend
from app.admin.views import UserAdmin, BookingsAdmin, HotelsAdmin, RoomsAdmin
from app.bookings.router import router as router_bookings
from app.database import engine
from app.hotels.router import router as router_hotels
from app.users.router import router as router_users
from app.rooms.router import router as router_rooms

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

from sqladmin import Admin, ModelView

app = FastAPI()

app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_users)
app.include_router(router_rooms)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_response=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)
