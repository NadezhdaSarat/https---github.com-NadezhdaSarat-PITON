from importlib.metadata.diagnose import inspect
from Subjecttable import SubjectTable
import pytest
from sqlalchemy import create_engine, text


db_connection_string = SubjectTable("postgresql://postgres:123@localhost:5432/postgres")
db = create_engine(db_connection_string, echo=True)

@pytest.fixture()

def test_db_connection():
  inspector = inspect(db)
  names = inspector.get_table_names()
  assert names[2] == 'subject_id'

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM subject"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['subject_id'] == 1
    assert row1['subject_title'] == "English"
    print(rows[0]["name"]) if rows else print("No results")
    connection.close()

def test_select_1_row():
  connection = db.connect()
  sql_statement = text("SELECT * FROM subject WHERE id = :subject_id")
  result = connection.execute(sql_statement, {"subject_id": 6})
  rows = result.mappings().all()
  assert len(rows) == 1
  assert rows[0]["subject_title"] == "Russian"
  connection.close()

def test_insert_subject():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("INSERT INTO subject(\"subject_title\") VALUES (:new_subject_title)")
    connection.execute(sql, {"new_subject_title":"Ecology"})
    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("UPDATE subject SET subject_title = :title WHERE subject_id = :subject_id")
    connection.execute(sql, {"title": 'New title', "subject_id": 16})
    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
    connection.execute(sql, {"subject_id": 16})
    transaction.commit()
    connection.close()

