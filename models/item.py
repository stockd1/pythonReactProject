from pydantic import BaseModel

class item(BaseModel):
    id: int
    name: str
    price: float