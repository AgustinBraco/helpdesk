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
- `USERNAME`
- `PASSWORD`
- `EMAIL`

### Crear migraciones

`python3 manage.py makemigrations`

### Migrar

`python3 manage.py migrate`

### Crear super usuario

`python3 manage.py createsuperuser`

---

## Ejecución

`python3 manage.py runserver`

---

## Apps

### Clientes

- Nombre: `clients`
- URLs: `/clients`
- Modelos: `Client` → `Company` & `Person`
- Vistas: `clients_all`
- Objetivo: Gestión de clientes (empresas y personas).

### Comentarios

- Nombre: `comments`
- URLs: `/comments`
- Modelos: `Comment`
- Vistas: `comments_all`
- Objetivo: Gestión de comentarios.

### Empleados

- Nombre: `employees`
- URLs: `/employees`
- Modelos: `Employees` & `EmployeeHistory`
- Vistas: `employees_all`
- Objetivo: Gestión de empleados e historial de asignaciones.

### Archivos

- Nombre: `files`
- URLs: `/files`
- Modelos: `Files`
- Vistas: `files_all`
- Objetivo: Gestión de archivos.

### Roles

- Nombre: `roles`
- URLs: `/roles`
- Modelos: `Rol` & `Permission` & `RolPermission`
- Vistas: `roles_all`
- Objetivo: Gestión de roles y permisos.

### Estados

- Nombre: `states`
- URLs: `/states`
- Modelos: `State` & `StateHistory`
- Vistas: `states_all`
- Objetivo: Gestión e historial de estados.

### Tickets

- Nombre: `tickets`
- URLs: `/tickets`
- Modelos: `Ticket`
- Vistas: `tickets_all`
- Objetivo: Gestión de tickets.

### Visitas

- Nombre: `visits`
- URLs: `/visits`
- Modelos: `Visit`
- Vistas: `visits_all`
- Objetivo: Gestión de visitas.

---
