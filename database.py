from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, Sequence, Text, create_engine, String, UUID, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

import config

import uuid

Base = declarative_base()


class Products(Base):
    __tablename__ = "Products"

    id = Column(Integer, Sequence("product_id_seq"), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False, default=100.0)
    count = Column(Integer, nullable=False)
    image = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    category_season = Column(String, nullable=False)
    category_clothing = Column(String, nullable=False)


engine = create_engine(config.DB_PATH, echo=config.DEBUG)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
