from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from ..settings import settings
from ..models.rdb.base import Base
from ..models.rdb.stock import *
from ..utils.logger import Logger


if not database_exists(settings.LOCAL_MYSQL_DATABASE_URI):
    Logger.i('rdb', f'Database not found. Creating database : {settings.LOCAL_MYSQL_DATABASE_URI}')
    create_database(settings.LOCAL_MYSQL_DATABASE_URI)

local_engine = create_engine(
    settings.LOCAL_MYSQL_DATABASE_URI,
    convert_unicode=True,
    pool_pre_ping=True
)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

local_db = LocalSession()
print(local_engine.table_names())


def init_rdb(recreate_table: bool = False) -> None:
    if recreate_table:
        drop_tables()
    Base.metadata.create_all(local_engine)


def show_tables() -> None:
    print(local_engine.table_names())


def drop_tables() -> None:
    Base.metadata.drop_all(local_engine)


def delete_all_tables() -> None:
    pass
