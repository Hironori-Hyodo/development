from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from datetime import datetime
import os
import sqlite3
import pandas as pd
import json
import uuid

router = APIRouter()

DB_FILE = "excel_data.db"
UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# DB 初期化（テーブルを削除して再作成）
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # 既存のテーブルを削除
    cursor.execute("DROP TABLE IF EXISTS screenshots")
    
    # 新しいテーブルを作成
    cursor.execute("""
        CREATE TABLE screenshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workbook_name TEXT,
            sheet_name TEXT,
            update_date TEXT,
            image BLOB
        )
    """)
    
    conn.commit()
    conn.close()

# **FastAPI 起動時にテーブルをリセット**
# init_db()


@router.post("/upload")
async def upload(files: UploadFile):
    print("Nice Upload! Post")

    contents = await files.read()

    #####################################
    # make class
    #####################################

    # Get current date
    dt = datetime.now()
    datetime_str = dt.strftime("%Y.%m.%d")

    # Excelの全シートを取得
    df_dict = pd.read_excel(BytesIO(contents), engine="openpyxl", sheet_name=None, header=None)  # ← header=None を指定

    # 各シートをリストのリストに変換
    sheets_data = {}
    for sheet_name, df in df_dict.items():
        sheets_data[sheet_name] = {
            "updateDate": datetime_str,
            "dataKind":"データ",
            "userName": "兵頭 弘訓",
            "data": df.fillna("").values.tolist(),  # ← NaN を空文字に置換し、2Dリストに変換
            "dataID": str(uuid.uuid4())
        }

    # 確認用
    print(json.dumps(sheets_data, indent=2, ensure_ascii=False))

    return JSONResponse({"sheets": sheets_data})