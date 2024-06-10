# Modelos de datos
from pydantic import BaseModel, ConfigDict

# Modelos de datos
class Author(BaseModel):
    id: int
    name: str
    birth_year: int

    model_config = ConfigDict(
        json_encoders={
            "Author": lambda v: v.model_dump(),
        }
    )

class Book(BaseModel):
    id: int
    title: str
    author_id: int
    year: int

    model_config = ConfigDict(
        json_encoders={
            "Book": lambda v: v.model_dump(),
        }
    )