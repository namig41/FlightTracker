from app.database import Base
from sqlalchemy import Column, Integer, String, JSON

class Hotels(Base):
    __tablename__ = 'moc_hotels.csv'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    services = Column(JSON)
    rooms_quantity = Column(Integer)
    stars = Column(Integer)


