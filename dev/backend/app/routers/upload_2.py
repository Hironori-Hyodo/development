from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse, Response
import openpyxl as op
from io import BytesIO
from datetime import datetime
import os
import sqlite3
import subprocess
import pandas as pd
import json

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
init_db()


@router.post("/upload")
async def upload(files: UploadFile):
    print("Nice Upload! Post")

    contents = await files.read()
    
    # Excelの全シートを取得
    df_dict = pd.read_excel(BytesIO(contents), engine="openpyxl", sheet_name=None)

    # 各シートをJSON化
    sheets_data = {}
    for sheet_name, df in df_dict.items():
        sheets_data[sheet_name] = json.loads(df.to_json(orient="records", force_ascii=False))

    print(sheets_data)  # 確認用ログ

    # return sheets_data  # { "Sheet1": [...], "Sheet2": [...], ... } の形式で返却

    return JSONResponse({"sheets": sheets_data})
