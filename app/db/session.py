from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# create engine; let SQLAlchemy choose driver options
connect_args = {}
if settings.DATABASE_URL is not None and settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
# test
engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


