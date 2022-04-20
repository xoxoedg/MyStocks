from sqlalchemy.exc import  OperationalError

from src.common.exception_handling import DatabaseNotLoadedError


def db_exception_handling(func):
    def wrapper(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
        except OperationalError:
            raise DatabaseNotLoadedError("Sorry the database was not initialized")

    return wrapper

