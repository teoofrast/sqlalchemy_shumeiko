from sqlalchemy import Column, Table, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()


































metadata_obj = MetaData()


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)
