from database import Products, session
from pydantic import BaseModel, Field, HttpUrl


def create_product(name: str, description: str, price: float, image, count: int, brand: str, category_season: str,
                   category_clothing: str) -> Products:
    product = Products(
        name=name,
        description=description,
        price=price,
        image=str(image),
        count=count,
        brand=brand,
        category_clothing=category_clothing,
        category_season=category_season
    )
    session.add(product)
    session.commit()
    return product


class NewProduct(BaseModel):
    name: str = Field(max_length=100, min_length=2)
    description: str = Field(max_length=100)
    price: float = Field(ge=0.01)
    image: HttpUrl


def get_all_product() -> list[NewProduct] | None:
    products = session.query(Products).all()
    return products


def get_product_by_brand(product_brand: str) -> list[Products] | None:
    product = session.query(Products).filter(Products.brand.ilike(f'%{product_brand}%')).all()
    return product


def get_product_by_price_diapason(min_price: int | float, max_price: int | float) -> list[Products] | None:
    product = session.query(Products).filter(float(max_price) > Products.price > float(min_price)).all()
    return product


def get_product_by_season(product_season: str) -> list[Products] | None:
    product = session.query(Products).filter(Products.category_season.ilike(f'%{product_season}%')).all()
    return product


def get_product_by_type(product_type: str) -> list[Products] | None:
    product = session.query(Products).filter(Products.category_clothing.ilike(f'%{product_type}%')).all()
    return product


def get_product_by_id(product_id: int) -> list[Products] | None:
    product = session.query(Products).filter(Products.id == product_id).all()
    return product



