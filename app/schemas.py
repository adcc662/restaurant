from pydantic import BaseModel


class RestaurantIn(BaseModel):
    """
    RestaurantIn is the schema for the data that is sent to the API.
    """
    id: str
    raiting: str
    name: str
    site: str
    email: str
    phone: str
    city: str
    street: str
    city: str
    state: str
    lat: str
    lng: str


class RestaurantDB(RestaurantIn):
    """
    RestaurantDB is the schema for the data that is stored in the database.
    """
    id: str

    class Config:
        """
        Configure the ORM mode to allow the data to be stored in the database.
        """
        orm_mode = True


class RestaurantOut(RestaurantDB):
    """
    RestaurantOut is the schema for the data that is sent back to the client.
    """
    pass
