from ninja import Schema

class TicketSchemaOut(Schema):
    id: int
    title: str
    description: str
    status: str

class TicketSchemaIn(Schema):
    title: str
    description: str