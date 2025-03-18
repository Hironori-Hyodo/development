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

# DB_FILE = "excel_data.db"
# UPLOAD_DIR = "temp"
# os.makedirs(UPLOAD_DIR, exist_ok=True)


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
            "data": df.fillna("").values.tolist()  # ← NaN を空文字に置換し、2Dリストに変換
        }

    # 確認用
    print(json.dumps(sheets_data, indent=2, ensure_ascii=False))

    return JSONResponse({"sheets": sheets_data})

    # # Get current date
    # dt = datetime.now()
    # datetime_str = dt.strftime("%Y.%m.%d")

    # # Excelの全シートを取得
    # df_dict = pd.read_excel(BytesIO(contents), engine="openpyxl", sheet_name=None)
    # # print(df_dict)
    

    # # 各シートをJSON化
    # sheets_data = {}
    # for sheet_name, df in df_dict.items():

    #     # もし `sheet_name` が `sheets_data` に存在しなければ、新しい辞書を作成
    #     if sheet_name not in sheets_data:
    #         sheets_data[sheet_name] = {}

    #     # `updateDate` と `data` をセット
    #     sheets_data[sheet_name]["updateDate"] = datetime_str
    #     sheets_data[sheet_name]["data"] = json.loads(df.to_json(orient="records", force_ascii=False))

    # print(json.dumps(sheets_data, indent=2, ensure_ascii=False))

    # return JSONResponse({"sheets": sheets_data})
