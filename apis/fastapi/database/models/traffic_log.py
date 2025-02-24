from database.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class TrafficLogModel(BaseModel):

    __tablename__ = "taffic_logs"

    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    host: Mapped[str] = mapped_column(nullable=False)
    client_ip: Mapped[str] = mapped_column(nullable=False)
    source_route: Mapped[str] = mapped_column(nullable=False)
    http_verb: Mapped[str] = mapped_column(nullable=False)
    headers: Mapped[str] = mapped_column(nullable=True)
    traffic_date: Mapped[str] = mapped_column(nullable=False)
    