from fastapi import FastAPI, Depends
from app.routes.restaurant import restaurant
from .controllers import extract
from sqlalchemy.orm import Session
from .database.database import engine, Base, get_db
from .models import restaurant as restaurant_model

app = FastAPI()

app.include_router(restaurant, prefix="/restaurant", tags=["restaurant"])
restaurant_model.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/extract")
async def extract_data(db: Session = Depends(get_db)):
    return extract.main(db)
