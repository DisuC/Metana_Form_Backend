# models.py
from sqlalchemy import Table, Column, Integer, String
from database import metadata

test_table = Table(
    "test_table",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(20)),
    Column("last_name", String(20)),
    Column("email", String(256)),
    Column("country", String(15)),
    Column("phone", String(15)),
    Column("languages", String(256)),
    Column("linkedin", String(256)),
    Column("experience", String(2)),
    Column("annual_compensation", String(2))
)

