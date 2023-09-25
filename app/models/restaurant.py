from sqlalchemy import (Column, Integer, String,
                        Float, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database.database import Base
import uuid


class Restaurant(Base):
    """
    Restaurant model
    """
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_csv = Column(UUID(as_uuid=True),default=uuid.uuid4)
    raiting = Column(Integer, nullable=False)
    name = Column(String(50), nullable=True)
    site = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    phone = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)
    street = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)
    state = Column(String(50), nullable=True)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)

    def __init__(self, raiting, name, site, email, phone,
                 city, street, state, lat, lng):
        self.raiting = raiting
        self.name = name
        self.site = site
        self.email = email
        self.phone = phone
        self.city = city
        self.street = street
        self.state = state
        self.lat = lat
        self.lng = lng
