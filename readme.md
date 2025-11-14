# Helpdesk

---

## Configuración

### Crear entorno virtual

`python3 -m venv env`

### Activar entorno virtual

`source env/bin/activate`

### Instalar dependencias

`pip install -r requirements.txt`

### Crear variables de entorno:

- `DJANGO_SECRET_KEY`
- `HOST`
- `SU_USERNAME`
- `SU_PASSWORD`
- `SU_EMAIL`

### Crear migraciones

`python3 manage.py makemigrations`

### Migrar

`python3 manage.py migrate`

### Crear super usuario por consola

`python3 manage.py createsuperuser`

### Crear super usuario por script

`python3 create_superuser.py`

---

## Ejecución

`python3 manage.py runserver`

---

## Apps

### Attachments

- URLs: `/attachments`
- Modelos: `Attachment`
- Vistas: `attachments_all`
- Objetivo: Gestión de archivos.

### Interactions

- URLs: `/interactions` - `/interactions/comments` - `/interactions/visits`
- Modelos: `Comment`, `Visit`
- Vistas: `interactions` - `comments` - `visits`
- Objetivo: Gestión de comentarios y visitas.

### Roles

- URLs: `/roles` - `/roles/employees` - `/roles/clients`
- Modelos: `Employee` - `Client`
- Vistas: `roles` - `employees` - `clients`
- Objetivo: Gestión de empleados y clientes.

### Tickets

- URLs: `/tickets` - `/tickets/tickets` - `/tickets/states` - `/tickets/ticket_history`
- Modelos: `Ticket` - `State` - `TicketHistory`
- Vistas: `tickets` - `ticket_history` - `states` - `tickets`
- Objetivo: Gestión de tickets, estados e historial de tickets.

### Users

- URLs: `/users` - `/users/contacts` - `/users/companies` - `/users/persons` -
- Modelos: `Contact` - `Company` - `Person`
- Vistas: `users` - `contacts` - `companies` - `persons`
- Objetivo: Gestión de contactos, compañias y personas.

---
