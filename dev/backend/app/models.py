from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# DB 設定（SQLiteを使用、PostgreSQLやMySQLに変更可能）
DATABASE_URL = "sqlite:///./excel.data.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# シート情報のテーブル
class SheetInfo(Base):
    __tablename__ = "sheet_info"
    id = Column(Integer, primary_key=True, index=True)
    sheet_name = Column(String, index=True)
    file_name = Column(String)  # 追加: 保存するExcelのファイル名
    min_row = Column(Integer)
    min_column = Column(Integer)
    max_row = Column(Integer)
    max_column = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# DB 初期化
def init_db():
    Base.metadata.create_all(bind=engine)
