from app.database.database import get_db
from app.models.restaurant import Restaurant
from sqlalchemy.orm import Session
import pandas as pd
import uuid

df = pd.read_csv('/app/app/controllers/restaurantes.csv')


def row_to_restaurant(row):
    """
    Convert a row to a Restaurant object
    """
    return Restaurant(
        raiting=row['rating'],
        name=row['name'],
        site=row['site'],
        email=row['email'],
        phone=row['phone'],
        street=row['street'],
        city=row['city'],
        state=row['state'],
        lat=row['lat'],
        lng=row['lng']
    )


def main(db: Session):

    df = pd.read_csv('/app/app/controllers/restaurantes.csv')

    db = next(get_db())

    for index, row in df.iterrows():
        restaurant = row_to_restaurant(row)
        db.add(restaurant)

    db.commit()

    db.close()


if __name__ == "__main__":
    main()
