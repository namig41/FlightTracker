from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey


class Rooms(Base):
    __tablename__ = 'moc_rooms.csv'

    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(ForeignKey("moc_hotels.csv.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)
