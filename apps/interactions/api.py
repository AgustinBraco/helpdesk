from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from tickets.models import Ticket, TicketHistory
from .models import Comment, Visit
from .schemas import (
    CommentCreate,
    CommentOut,
    VisitCreate,
    VisitOut,
)

router = Router(tags=["interactions"])

@router.get("/tickets/{ticket_id}/comments", response=List[CommentOut])
def list_comments_by_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    histories = ticket.ticket_history.all()
    return Comment.objects.filter(id_history__in=histories)

@router.post("/tickets/{ticket_id}/comments", response=CommentOut)
def create_comment_for_ticket(request, ticket_id: int, payload: CommentCreate):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    last_history = ticket.ticket_history.order_by("-timestamp").first()

    if last_history is None:
        last_history = TicketHistory.objects.create(
            id_ticket=ticket,
            id_employee_id=1,
        )

    comment = Comment.objects.create(
        id_history=last_history,
        content=payload.content,
    )

    return comment


@router.get("/tickets/{ticket_id}/visits", response=List[VisitOut])
def list_visits_by_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    histories = ticket.ticket_history.all()
    return Visit.objects.filter(id_history__in=histories)


@router.post("/tickets/{ticket_id}/visits", response=VisitOut)
def create_visit_for_ticket(request, ticket_id: int, payload: VisitCreate):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    last_history = ticket.ticket_history.order_by("-timestamp").first()

    if last_history is None:
        last_history = TicketHistory.objects.create(
            id_ticket=ticket,
            id_employee_id=1,
        )

    visit = Visit.objects.create(
        id_history=last_history,
        content=payload.content,
    )

    return visit
