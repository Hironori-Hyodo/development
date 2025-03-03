from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def read_user():
  return [{"id":1,"name":"Tanaka"},{"id":2,"name":"Nakanishi"}]
