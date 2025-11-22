from ninja import Schema
from datetime import datetime
from typing import Optional
from pydantic import Field

class TicketSchemaIn(Schema):
    id_client: int
    priority: str
    title: str
    description: str

class TicketSchemaOut(Schema):
    id: int
    id_client: int = Field(..., alias="id_client_id")
    priority: str
    title: str
    description: str
    created_at: datetime
    closed_at: Optional[datetime] = None

class StateOut(Schema):
    id: int
    id_ticket: int = Field(..., alias="id_ticket_id")
    state: str
    created_at: datetime

class StateChangeIn(Schema):
    state: str
    id_employee: int

class TicketHistoryOut(Schema):
    id: int
    id_ticket: int = Field(..., alias="id_ticket_id")
    id_employee: int = Field(..., alias="id_employee_id")
    timestamp: datetime