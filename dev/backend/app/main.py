from fastapi import FastAPI
from routers import users,items,upload,upload_2
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

origins = [
  "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def roo():
  return {"message": "Hello World!!"}

app.include_router(users.router,prefix="/api")
app.include_router(items.router,prefix="/api")
# app.include_router(upload.router, prefix="/api")
app.include_router(upload_2.router, prefix="/api")