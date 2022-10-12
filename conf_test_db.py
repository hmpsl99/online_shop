from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database
from main import app

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test_database.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args = {"check_same_thread":False})

TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)


database.Base.metadata.drop_all(bind=engine)
database.Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    

app.dependency_overrides[database.get_db] = override_get_db