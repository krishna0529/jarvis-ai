# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine

from memory.config import SQLITE_DB

engine = create_engine(

    f"sqlite:///{SQLITE_DB}"

)
