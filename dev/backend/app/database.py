from sqlalchemy.orm import Session
from models import SessionLocal

# DB セッションを取得
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
