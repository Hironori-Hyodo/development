from fastapi import FastAPI
from routers import users,items
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

origins = [
  "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def roo():
  return {"message": "Hello World!!"}

app.include_router(users.router,prefix="/api")
app.include_router(items.router,prefix="/api")
