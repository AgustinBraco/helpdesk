from typing import List, Optional

from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Ticket, State, TicketHistory
from .schemas import (
    TicketCreate,
    TicketUpdate,
    TicketOut,
    StateOut,
    StateChangeIn,
    TicketHistoryOut,
)

router = Router(tags=["tickets"])

@router.get("/tickets", response=List[TicketOut])
def list_tickets(request, priority: Optional[str] = None):
    qs = Ticket.objects.all()
    if priority:
        qs = qs.filter(priority=priority)
    return qs

@router.get("/tickets/{ticket_id}", response=TicketOut)
def get_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket

@router.post("/tickets", response=TicketOut)
def create_ticket(request, payload: TicketCreate):
    ticket = Ticket.objects.create(
        id_client_id=payload.id_client,
        priority=payload.priority,
        title=payload.title,
        description=payload.description,
    )
    return ticket

@router.put("/tickets/{ticket_id}", response=TicketOut)
def update_ticket(request, ticket_id: int, payload: TicketUpdate):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(ticket, attr, value)

    ticket.save()
    return ticket

@router.delete("/tickets/{ticket_id}")
def delete_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return {"success": True}

@router.get("/tickets/{ticket_id}/states", response=List[StateOut])
def list_states(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket.states.all()

@router.post("/tickets/{ticket_id}/states", response=StateOut)
def change_state(request, ticket_id: int, payload: StateChangeIn):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    state = State.objects.create(
        id_ticket=ticket,
        state=payload.state,
    )

    TicketHistory.objects.create(
        id_ticket=ticket,
        id_employee_id=payload.id_employee,
    )

    return state

@router.get("/tickets/{ticket_id}/history", response=List[TicketHistoryOut])
def list_history(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket.ticket_history.all()
