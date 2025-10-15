import pytest
from subject_table import SubjectTable

connection_string = "postgresql://postgres:123@localhost:5432/postgres"
db = SubjectTable(connection_string)

def test_create_subject():
    db.create("EcologyTest")
    subjects = db.get_all()
    assert any(s["subject_title"] == "EcologyTest" for s in subjects)
    for s in subjects:
        if s["subject_title"] == "EcologyTest":
    db.delete(s["subject_id"])

def test_update_subject():
    db.create("TempTitle")
    subjects = db.get_all()
    temp_id = next(s["subject_id"] for s in subjects if s["subject_title"] == "TempTitle")
    db.update(temp_id, "UpdatedTitle")
    updated = db.get_all()
    assert any(s["subject_title"] == "UpdatedTitle" and s["subject_id"] == temp_id for s in updated)
    db.delete("temp_id")

def test_delete_subject():
    db.create("ToDelete")
    subjects = db.get_all()
    del_id = next(s["subject_id"] for s in subjects if s["subject_title"] == "ToDelete")
    db.delete(del_id)
    after = db.get_all()
    assert all(s["subject_id"] != del_id for s in after)
