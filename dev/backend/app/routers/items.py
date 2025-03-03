from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def item_list():
  return [{"id":1,"name":"Super_belt","price":121},{"id":2,"name":"Normal_belt","price":34}]
