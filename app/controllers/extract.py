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
        id=row['id'],
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
    # Lee el archivo CSV
    df = pd.read_csv('/app/app/controllers/restaurantes.csv')

    # Obtén una sesión de la base de datos
    db = next(get_db())

    # Itera sobre las filas del DataFrame y agrega registros a la base de datos
    for index, row in df.iterrows():
        restaurant = row_to_restaurant(row)
        db.add(restaurant)

    # Realiza un commit de los cambios
    db.commit()

    # Cierra la sesión de base de datos
    db.close()


if __name__ == "__main__":
    main()
