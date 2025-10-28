## Installation and execution

### Create virtual environment:
`python3 -m venv env`

### Activate virtual environment:
`source env/bin/activate`

### Install dependencies:
`pip install -r requirements.txt`

### Run server:
`python3 manage.py runserver`

-----

## Configuration

### Create app:
`python3 manage.py startapp name apps/name`

### Make migrations:
`python3 manage.py makemigrations`

### Migrate:
`python3 manage.py migrate`

### Create super user:
`python3 manage.py createsuperuser`

-----

## Information

### Apps:
- `accounts` → Usuarios, roles y permisos.
- `clients` → Todo relacionado a clientes.
- `tickets` → Estados e historial de estados + Información e historial de asignados.
- `comments` → Comentarios e historial de comentarios.
- `visits` → Visitas e historial de visitas.
- `files` → Archivos e historial de archivo


### URLs:
```
.../admin
.../accounts
.../clients
.../comments
.../files
.../tickets
.../visits
```

