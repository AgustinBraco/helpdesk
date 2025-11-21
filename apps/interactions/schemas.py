from ninja import Schema, Field
from datetime import datetime

class CommentCreate(Schema):
    content: str

class CommentOut(Schema):
    id: int
    id_history: int = Field(..., alias="id_history_id")
    content: str
    created_at: datetime

class VisitCreate(Schema):
    content: str

class VisitOut(Schema):
    id: int
    id_history: int = Field(..., alias="id_history_id")
    content: str
    created_at: datetime