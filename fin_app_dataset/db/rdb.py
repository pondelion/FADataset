from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database, drop_database

from ..settings import settings
from ..models.rdb.base import Base
from ..models.rdb.stock import (
    CompanyModel,
    SectorModel,
    StqDailyStockpriceModel,
    YFDailyStockpriceModel,
)
from ..models.rdb.news import (
    GoogleNewsModel,
)
from ..models.rdb.financial import (
    YFFinancialModel,
)
from ..utils.logger import Logger


def delete_database() -> None:
    if database_exists(settings.LOCAL_MYSQL_DATABASE_URI):
        Logger.i('rdb', f'Deleting database : {settings.LOCAL_MYSQL_DATABASE_URI}')
        drop_database(settings.LOCAL_MYSQL_DATABASE_URI)


def create_databse() -> None:
    if not database_exists(settings.LOCAL_MYSQL_DATABASE_URI):
        Logger.i('rdb', f'Database not found. Creating database : {settings.LOCAL_MYSQL_DATABASE_URI}')
        create_database(settings.LOCAL_MYSQL_DATABASE_URI)


def init_rdb(
    recreate_database: bool = False,
    recreate_table: bool = False
) -> None:
    if recreate_database:
        delete_database()
    create_databse()
    if recreate_table:
        drop_tables()
    Base.metadata.create_all(local_engine)


create_databse()

local_engine = create_engine(
    settings.LOCAL_MYSQL_DATABASE_URI,
    convert_unicode=True,
    pool_pre_ping=True
)

LocalSession = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=local_engine))
# Base.query = LocalSession.query_property()

local_db = LocalSession()
init_rdb()
print(local_engine.table_names())


def show_tables() -> None:
    print(local_engine.table_names())


def drop_tables() -> None:
    # Base.metadata.drop_all(local_engine)
    try:
        StqDailyStockpriceModel.__table__.drop(local_engine)
    except Exception as e:
        print(e)
    try:
        YFDailyStockpriceModel.__table__.drop(local_engine)
    except Exception as e:
        print(e)
    try:
        CompanyModel.__table__.drop(local_engine)
    except Exception as e:
        print(e)
    try:
        SectorModel.__table__.drop(local_engine)
    except Exception as e:
        print(e)
    try:
        Base.metadata.drop_all(local_engine)
    except Exception as e:
        print(e)


def delete_all_tables() -> None:
    pass
