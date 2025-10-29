# FastOpp - Basic Introduction to ORM

Code for tutorial for basic introduction to ORM using the [FastOpp](https://github.com/Oppkey/fastopp)
system.

- [Beginner Python ORM with SQLAlchemy Tutorial](https://youtu.be/V1R2w38Jqsg)

## Installation

```bash
uv sync
```

## Setup

Create database.

`uv run python oppman.py db`

Create superuser.

`uv run python oppman.py superuser`

### Initialize Database for Migrations

```bash
uv run python oppman.py migrate init
uv run python oppman.py makemigrations
uv run python oppman.py migrate upgrade
```

## Run Development Server

```bash
uv run python oppman.py runserver
```

Visit `http://localhost:8000`

## Access Admin Panel

Visit `http://localhost:8000/admin`

Login as `admin@example.com`, `admin123`.

Create sample data.

## Troubleshooting

If the migration fails:

```
rm -rf alembic/versions/*
rm -rf alembic/__pycache__/*
uv run python oppman.py migrate create
uv run python oppman.py upgrade
```

if this still fails:

```
uv run oppman.py delete
uv run python oppman.py db
uv run python oppman.py superuser
uv run python oppman.py migrate init
uv run python oppman.py makemigrations
uv run python oppman.py migrate upgrade
```
