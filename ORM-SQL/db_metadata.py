from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from random_data_generator import RandomData
from sqlalchemy import insert
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    f_name: Mapped[str] = mapped_column(String(30))
    l_name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)
    full_name: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

class Address(Base):
    __tablename__ = "address_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email_address: Mapped[str] = mapped_column(String)
    user_id = mapped_column(ForeignKey("user_table."))

    user: Mapped[List["User"]] = relationship(back_populates="addresses")

def populate_data() -> None:
    engine = create_engine("sqlite+pysqlite:///instances/myusers.db", echo=True)
    data_obj = RandomData(200)
    with Session(engine) as session:
        result = session.execute(insert(User).values(data_obj.data))
        session.commit()

populate_data()
