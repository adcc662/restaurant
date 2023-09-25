from pydantic import BaseModel
import uuid


class RestaurantIn(BaseModel):
    """
    RestaurantIn is the schema for the data that is sent to the API.
    """
    raiting: int
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    lat: float
    lng: float


class RestaurantDB(RestaurantIn):
    """
    RestaurantDB is the schema for the data that is stored in the database.
    """
    id: int

    class Config:
        """
        Configure the ORM mode to allow the data to be stored in the database.
        """
        from_attributes = True


class RestaurantOut(RestaurantDB):
    """
    RestaurantOut is the schema for the data that is sent back to the client.
    """
    pass
