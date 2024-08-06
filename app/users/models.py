from app.database import Base
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'moc_users.csv'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    hashed_password = Column(String)

    booking = relationship("Bookings", back_populates="booking")

    def __str__(self):
        return f"User #{self.email}"
