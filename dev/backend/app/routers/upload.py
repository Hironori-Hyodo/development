
from fastapi import APIRouter,File,Form,UploadFile,Request,HTTPException
from fastapi.responses import JSONResponse
import openpyxl as op
from io import BytesIO
# from fastapi import APIRouter, File, UploadFile, HTTPException
# from fastapi.responses import JSONResponse
# from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import openpyxl
# from io import BytesIO

# router = APIRouter()

# # --- DB 設定 (SQLite) ---
# DATABASE_URL = "sqlite:///./excel_data.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # --- Excel データ保存用の DB モデル ---
# class ExcelFile(Base):
#     __tablename__ = "excel_files"
#     id = Column(Integer, primary_key=True, index=True)
#     filename = Column(String, index=True)
#     data = Column(LargeBinary)  # Excel ファイルをバイナリデータとして保存

# # --- DB のテーブル作成 ---
# Base.metadata.create_all(bind=engine)

# # --- 文字のある範囲（左上・右下座標）を取得する関数 ---
# def get_text_bounds(sheet):
#     min_row, min_col, max_row, max_col = None, None, None, None

#     for row in sheet.iter_rows():
#         for cell in row:
#             if cell.value is not None:
#                 if min_row is None or cell.row < min_row:
#                     min_row = cell.row
#                 if min_col is None or cell.column < min_col:
#                     min_col = cell.column
#                 if max_row is None or cell.row > max_row:
#                     max_row = cell.row
#                 if max_col is None or cell.column > max_col:
#                     max_col = cell.column

#     if min_row is None or min_col is None or max_row is None or max_col is None:
#         return None  # データがない場合

#     return {"leftup": [min_row - 1, min_col - 1], "rightdown": [max_row - 1, max_col - 1]}

# # --- エクセルファイルを受け取るエンドポイント ---
# @router.post("/upload")
# async def upload_excel(file: UploadFile = File(...)):
#     try:
#         # --- 受け取ったファイルの情報をログに出力 ---
#         print(f"ファイルを受け取りました: {file.filename}")

#         # --- Excel をメモリ上で開く ---
#         contents = await file.read()
#         excel_data = BytesIO(contents)
#         wb = openpyxl.load_workbook(excel_data, data_only=True)

#         # --- 各シートのデータ範囲を取得 ---
#         sheets_bounds = {}
#         for sheet_name in wb.sheetnames:
#             sheet = wb[sheet_name]
#             bounds = get_text_bounds(sheet)
#             sheets_bounds[sheet_name] = bounds if bounds else "No Data"

#         # --- DB にファイル保存 ---
#         db = SessionLocal()
#         db_excel = ExcelFile(filename=file.filename, data=contents)
#         db.add(db_excel)
#         db.commit()
#         db.close()

#         # --- JSON 形式でフロントエンドへ返却 ---
#         return JSONResponse(content={"sheets": sheets_bounds, "message": "ファイルを受信しました"})
    
#     except Exception as e:
#         print(f"エラー発生: {str(e)}")  # エラーメッセージをログ出力
#         raise HTTPException(status_code=500, detail=f"エラー: {str(e)}")

router = APIRouter()

@router.post("/upload")
async def upload(files:UploadFile):
    print("Nice Upload! Post")

    workbook_name = files.filename
    print(workbook_name)

    # allow mime list
    ALLOWED_MIME_TYPES = [
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # .xlsx
        "application/vnd.ms-excel.sheet.macroEnabled.12",  # .xlsm
        "application/vnd.ms-excel.sheet.binary.macroEnabled.12",  # .xlsb
        "application/vnd.openxmlformats-officedocument.spreadsheetml.template",  # .xltx
        "application/vnd.ms-excel",  # .xlt (Excel 97-2003 Template)
        "application/vnd.ms-excel.addin.macroEnabled.12",  # .xlam
    ]

    # Readable only Excel file
    if files.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400,detail="無効なファイル形式です。\nExcelファイルをアップロードしてください。")
    
    contents = await files.read()

    try:
        workbook = op.load_workbook(BytesIO(contents))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400,detail="Excelファイルの読み込みに失敗しました。\nファイルが破損している可能性があります。\nシステム管理者にご連絡ください。")
    
    print(workbook.sheetnames)

    sheets_data = {}
    for sheet_name in workbook.sheetnames:
        # 左上(min-row * min-colomn)と右下(max-row * max-column)を取得
        ws = workbook[sheet_name]

        min_flg = False
        for row in ws.iter_rows():
            for cell in row:
                if cell.value is not None:
                    print(cell.value)
                    if min_flg == False:
                        min_row = max_row = cell.row
                        min_column = max_column = cell.column
                        min_flg = True
                    if max_row < cell.row:
                        max_row = cell.row
                    if max_column < cell.column:  
                        max_column = cell.column
        
        print("最小",min_row,min_column)
        print("最大",max_row,max_column)

    return JSONResponse({"Msg":"Nice"})

