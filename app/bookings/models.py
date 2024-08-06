from app.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import relationship


class Bookings(Base):
    __tablename__ = 'moc_bookings.csv'

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(ForeignKey("moc_rooms.csv.id"))
    user_id = Column(ForeignKey("moc_users.csv.id"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(date_from - date_to) * price"))
    total_days = Column(Integer, Computed("date_from - date_to"))

    booking = relationship("Users", back_populates="booking")

    def __str__(self):
        return f"Booking #{self.id}"
