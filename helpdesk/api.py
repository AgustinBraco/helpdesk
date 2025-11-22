from ninja import NinjaAPI
from django.shortcuts import get_object_or_404

from apps.tickets.models import Ticket, State, TicketHistory
from apps.roles.models import Client, Employee
from apps.interactions.models import Comment, Visit

from apps.tickets.schemas import (
    TicketSchemaOut,
    TicketSchemaIn,
    StateOut,
    StateChangeIn,
    TicketHistoryOut,
)
from apps.interactions.schemas import (
    CommentCreate,
    CommentOut,
    VisitCreate,
    VisitOut,
)

api = NinjaAPI()

# ========================
#        TICKETS
# ========================

@api.get("/tickets", response=list[TicketSchemaOut])
def list_tickets(request):
    return Ticket.objects.all()


@api.get("/tickets/{ticket_id}", response=TicketSchemaOut)
def get_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket


@api.post("/tickets", response=TicketSchemaOut)
def create_ticket(request, data: TicketSchemaIn):

    client = get_object_or_404(Client, id=data.id_client)

    ticket = Ticket.objects.create(
        id_client=client,
        priority=data.priority,
        title=data.title,
        description=data.description,
    )

    return ticket


@api.put("/tickets/{ticket_id}", response=TicketSchemaOut)
def update_ticket(request, ticket_id: int, data: TicketSchemaIn):

    ticket = get_object_or_404(Ticket, id=ticket_id)

    client = get_object_or_404(Client, id=data.id_client)

    ticket.id_client = client
    ticket.priority = data.priority
    ticket.title = data.title
    ticket.description = data.description

    ticket.save()
    return ticket

@api.delete("/tickets/{ticket_id}")
def delete_ticket(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return {"success": True}


# ========================
#       STATES
# ========================

@api.get("/tickets/{ticket_id}/states", response=list[StateOut])
def list_states(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket.states.all()


@api.post("/tickets/{ticket_id}/states", response=StateOut)
def change_state(request, ticket_id: int, data: StateChangeIn):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    new_state = State.objects.create(
        id_ticket=ticket,
        state=data.state
    )

    employee = get_object_or_404(Employee, id=data.id_employee)

    TicketHistory.objects.create(
        id_ticket=ticket,
        id_employee=employee
    )

    return new_state


# ========================
#      HISTORY
# ========================

@api.get("/tickets/{ticket_id}/history", response=list[TicketHistoryOut])
def get_history(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return ticket.ticket_history.all()


# ========================
#      COMMENTS
# ========================

@api.get("/tickets/{ticket_id}/comments", response=list[CommentOut])
def list_comments(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    histories = ticket.ticket_history.all()
    return Comment.objects.filter(id_history__in=histories)


@api.post("/tickets/{ticket_id}/comments", response=CommentOut)
def create_comment(request, ticket_id: int, data: CommentCreate):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    last_history = ticket.ticket_history.order_by("-timestamp").first()

    if last_history is None:
        last_history = TicketHistory.objects.create(
            id_ticket=ticket,
            id_employee_id=1
        )

    comment = Comment.objects.create(
        id_history=last_history,
        content=data.content
    )

    return comment


# ========================
#       VISITS
# ========================

@api.get("/tickets/{ticket_id}/visits", response=list[VisitOut])
def list_visits(request, ticket_id: int):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    histories = ticket.ticket_history.all()
    return Visit.objects.filter(id_history__in=histories)


@api.post("/tickets/{ticket_id}/visits", response=VisitOut)
def create_visit(request, ticket_id: int, data: VisitCreate):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    last_history = ticket.ticket_history.order_by("-timestamp").first()

    if last_history is None:
        last_history = TicketHistory.objects.create(
            id_ticket=ticket,
            id_employee_id=1
        )

    visit = Visit.objects.create(
        id_history=last_history,
        content=data.content
    )

    return visit
