import os
import sqlalchemy
from databases import Database
from infrastructure.postgresql_repo import metadata

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/tododb")

database = Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL.replace("+asyncpg", ""))


def init_db():
    metadata.create_all(engine)
