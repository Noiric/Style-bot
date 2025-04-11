from database import Products, session
from pydantic import BaseModel, Field, HttpUrl


def create_product(name: str, description: str, price: float, image, count: int, category_season: str,
                   category_clothing: str) -> Products:
    product = Products(
        name=name,
        description=description,
        price=price,
        image=str(image),
        count=count,
        category_clothing=category_clothing,
        category_season=category_season
    )
    session.add(product)
    session.commit()
    return product


def get_all_product() -> list[Products]:
    products = session.query(Products).all()
    return products


def get_product_by_name(product_name: str) -> list[Products]:
    product = session.query(Products).filter(Products.name.ilike(f'%{product_name}%')).all()
    return product


def get_product_by_price(product_price: int | float) -> list[Products]:
    product = session.query(Products).filter(Products.price == float(product_price)).all()
    return product


def get_product_by_season(product_season: str) -> list[Products]:
    product = session.query(Products).filter(Products.category_season == product_season).all()
    return product


def get_product_by_type(product_type: str) -> list[Products]:
    product = session.query(Products).filter(Products.category_clothing == product_type).all()
    return product


def get_product_by_id(product_id: int) -> list[Products]:
    product = session.query(Products).filter(Products.id == product_id).all()
    return product



