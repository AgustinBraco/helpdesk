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
- `DEBUG`

# Base de Datos PostgreSQL
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

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

- Gestión de archivos.
- Modelos:

```
Attachment
```

### Interactions

- Gestión de comentarios y visitas.
- Modelos:

```
Comment
Visit
```

### Roles

- Gestión de empleados y clientes.
- Modelos:

```
Employee
Client
```

### Tickets

- Gestión de tickets, estados e historial de tickets.

- Modelos:

```
Ticket
State
TicketHistory
```

- URLs:

```
/tickets
/tickets/:id
/tickets/create
```

- Vistas:

```
/tickets
/tickets/:id
/tickets/create
```

### Users

- Gestión de contactos, compañias y personas.
- Modelos:

```
Contact
Company
Person
```

- URLs:

```
/login
/logout
```

- Vistas:

```
/login
```

---

## Modelos

### Attachment

- id_history: ForeignKey
- content: FileField
- created_at: DateTimeField

### Comment

- id_history: ForeignKey
- content: TextField
- created_at: DateTimeField

### Visit

- id_history: ForeignKey
- content: TextField
- created_at: DateTimeField

### Employee

- id_person: ForeignKey
- id_contact: ForeignKey
- tax_id: CharField
- role: CharField

### Client

- id_person: ForeignKey
- id_contact: ForeignKey
- id_company: ForeignKey
- tax_id: CharField
- role: CharField

### Ticket

- id_client: ForeignKey
- priority: CharField
- title: CharField
- description: TextField
- created_at: DateTimeField
- closed_at: DateTimeField

### State

- id_ticket: ForeignKey
- state: CharField
- created_at: DateTimeField

### TicketHistory

- id_ticket: ForeignKey
- id_employee: ForeignKey
- timestamp: DateTimeField

### Contact

- email: CharField
- password: TextField
- phone: CharField

### Company

- name: CharField

### Person

- first_name: CharField
- last_name: CharField
- birthday: DateField

---

## Redirecciones

### Home

- Logeado ➜ Tickets
- NO logeado ➜ Login

### Login

- Logeado ➜ Tickets
- NO logeado ➜ Login

### Logout

- Logeado ➜ Login
- NO logeado ➜ Login

### Tickets

- Logeado ➜ Login
- NO logeado ➜ Login

---

## Gracias!
