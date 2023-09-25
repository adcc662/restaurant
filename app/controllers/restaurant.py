from app.models.restaurant import Restaurant
from sqlalchemy.orm import Session
from functools import lru_cache
from sqlalchemy import func
from math import (radians, sin, cos, sqrt)
import uuid


async def get_restaurants_statistics(db: Session, latitude: float, longitude: float, radius: int):
    """
    Get restaurants statistics
    """
    radius_degrees = radius / 111300
    min_lat = latitude - radius_degrees
    max_lat = latitude + radius_degrees
    min_lng = longitude - radius_degrees
    max_lng = longitude + radius_degrees

    count = db.query(func.count(Restaurant.id)).filter(
        Restaurant.lat.between(min_lat, max_lat),
        Restaurant.lng.between(min_lng, max_lng)
    ).scalar()

    avg_raiting = db.query(func.avg(Restaurant.raiting)).filter(
        Restaurant.lat.between(min_lat, max_lat),
        Restaurant.lng.between(min_lng, max_lng)
    ).scalar()

    std_raiting = db.query(func.stddev(Restaurant.raiting)).filter(
        Restaurant.lat.between(min_lat, max_lat),
        Restaurant.lng.between(min_lng, max_lng)
    ).scalar()

    if count is None:
        count = 0
    if avg_raiting is None:
        avg_raiting = 0
    if std_raiting is None:
        std_raiting = 0

    return {
        "count": count,
        "avg": avg_raiting,
        "std": std_raiting
    }


async def create_restaurant(data: dict, db: Session):
    """
    Create a new restaurant
    """
    new_restaurant = Restaurant(**data)

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant


@lru_cache
async def get_all_restaurants(db: Session):
    """
    Get all restaurants
    """
    return db.query(Restaurant).all()


@lru_cache
async def get_restaurant_by_id(id: int, db: Session):
    """
    Get a restaurant by id
    """
    return db.query(Restaurant).filter(Restaurant.id == id).first()


async def update_restaurant(id: int, data: dict, db: Session):
    """
    Update a restaurant by id
    """
    db.query(Restaurant).filter(Restaurant.id == id).update(data)
    db.commit()
    return db.query(Restaurant).filter(Restaurant.id == id).first()


async def delete_restaurant(id: int, db: Session):
    """
    Delete a restaurant by id
    """
    restaurant = db.query(Restaurant).filter(Restaurant.id == id).first()
    db.delete(restaurant)
    db.commit()
    return restaurant


@lru_cache
async def get_all_restaurants_pagination(db: Session, page: int, limit: int):
    """
    Get all restaurants with pagination
    """
    return db.query(Restaurant).offset(page).limit(limit).all()
