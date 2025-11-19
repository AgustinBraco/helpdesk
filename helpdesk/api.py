from ninja import NinjaAPI
from apps.tickets.models import Ticket
from apps.tickets.schemas import TicketSchemaOut, TicketSchemaIn
from django.shortcuts import get_object_or_404

api = NinjaAPI()

# LISTAR tickets
@api.get("/tickets", response=list[TicketSchemaOut])
def list_tickets(request):
    return Ticket.objects.all()

# OBTENER 1 ticket por ID
@api.get("/tickets/{ticket_id}", response=TicketSchemaOut)
def get_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket

# CREAR un ticket
@api.post("/tickets", response=TicketSchemaOut)
def create_ticket(request, data: TicketSchemaIn):
    ticket = Ticket.objects.create(**data.dict())
    return ticket

# EDITAR un ticket
@api.put("/tickets/{ticket_id}", response=TicketSchemaOut)
def update_ticket(request, ticket_id: int, data: TicketSchemaIn):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    for attr, value in data.dict().items():
        setattr(ticket, attr, value)
    ticket.save()
    return ticket

# BORRAR un ticket
@api.delete("/tickets/{ticket_id}")
def delete_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return {"success": True}
