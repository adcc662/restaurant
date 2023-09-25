from fastapi import (APIRouter, HTTPException,
                     Request, Depends)
from app.schemas import (RestaurantIn,
                         RestaurantOut, RestaurantDB)
from app.controllers.restaurant import (create_restaurant,
                                        get_all_restaurants,
                                        get_restaurant_by_id,
                                        update_restaurant,
                                        delete_restaurant,
                                        get_all_restaurants_pagination,
                                        get_restaurants_statistics)
from app.database.database import get_db
from sqlalchemy.orm import Session

restaurant = APIRouter()


@restaurant.get("/", response_model=list[RestaurantOut])
async def get_all_restaurants_api(db: Session = Depends(get_db)):
    """
    Get all restaurants
    """
    restaurants = await get_all_restaurants(db)
    return restaurants


@restaurant.get("/statistics", response_model=dict)
async def get_restaurants_statistics_api(latitude: float, longitude: float, radius: int,
                                         db: Session = Depends(get_db)):
    """
    Get restaurants statistics
    """
    statistics = await get_restaurants_statistics(db, latitude, longitude, radius)
    if statistics is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return statistics


@restaurant.get("/pagination", response_model=list[RestaurantOut])
async def get_all_restaurants_pagination_api(db: Session = Depends(get_db),
                                             page: int = 0, limit: int = 10):
    """
    Get all restaurants with pagination
    """
    restaurants = await get_all_restaurants_pagination(db, page, limit)
    return restaurants


@restaurant.get("/{id}", response_model=RestaurantOut)
async def get_restaurant_by_id_api(id: int, db: Session = Depends(get_db)):
    """
    Get a restaurant by id routes
    """
    restaurant = await get_restaurant_by_id(id, db)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@restaurant.post("/", response_model=RestaurantOut)
async def create_restaurant_api(data: RestaurantIn, db: Session = Depends(get_db)):
    """
    Create a new restaurant
    """
    if data.raiting > 4:
        raise HTTPException(
            status_code=400, detail="Raiting must be less or equal to 4")
    restaurant = await create_restaurant(data.model_dump(), db)
    return restaurant


@restaurant.put("/{id}", response_model=RestaurantOut)
async def update_restaurant_api(id: int, data: RestaurantIn, db: Session = Depends(get_db)):
    """
    Update a restaurant by id
    """
    if data.raiting > 4:
        raise HTTPException(
            status_code=400, detail="Raiting must be less or equal to 4")
    restaurant = await update_restaurant(id, data.dict(), db)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@restaurant.delete("/{id}", response_model=RestaurantOut)
async def delete_restaurant_api(id: int, db: Session = Depends(get_db)):
    """
    Delete a restaurant by id
    """
    restaurant_delete = await delete_restaurant(id, db)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant_delete
