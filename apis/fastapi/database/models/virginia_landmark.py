from database.models.base import BaseModel
from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column


class VirginiaLandmarkModel:

    __tablename__ = "taffic_logs" 

    id: Mapped[int] = mapped_column(primary_key=True, index=True) 
    object_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    landmark_name: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=True)  
    city: Mapped[str] = mapped_column(nullable=True)
    state: Mapped[str] = mapped_column(nullable=True)  
    zip: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(nullable=True)
    latitude: Mapped[Float] = mapped_column(nullable=False)
    longitude: Mapped[Float] = mapped_column(nullable=False)
    location_type: Mapped[str] = mapped_column(nullable=False)
    location_county: Mapped[str] = mapped_column(nullable=False)
