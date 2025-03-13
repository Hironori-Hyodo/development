
from fastapi import APIRouter,File,Form,UploadFile,Request,HTTPException
from fastapi.responses import JSONResponse
import openpyxl as op
from io import BytesIO
from models import init_db
from datetime import datetime

router = APIRouter()

# DB init
# init_db()

# UPLOAD_FOLDER = "uploaded_excels"

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

    # Get current date
    dt = datetime.now()
    datetime_str = dt.strftime("%Y.%m.%d")

    sheets_data = []
    for sheet_name in workbook.sheetnames:
        # 左上(min-row * min-colomn)と右下(max-row * max-column)を取得
        ws = workbook[sheet_name]

        not_empty_cells = [cell for row in ws.iter_rows() for cell in row if cell.value is not None]
        # print(not_empty_cells)

        if not_empty_cells:
            min_row = min([cell.row for cell in not_empty_cells])
            max_row = max([cell.row for cell in not_empty_cells])
            min_column = min([cell.column for cell in not_empty_cells])
            max_column = max([cell.column for cell in not_empty_cells])

            for merged_range in ws.merged_cells:
                # print(merged_range)
                minr,minc,maxr,maxc = merged_range.min_row,merged_range.min_col,merged_range.max_row,merged_range.max_col
                max_row = max(max_row, maxr)
                max_column = max(max_column, maxc)

        sheets_data.append({
            "sheet_name":sheet_name,
            "update_date":datetime_str
        })

    print(sheets_data)

    
    return JSONResponse({"sheets":sheets_data})

