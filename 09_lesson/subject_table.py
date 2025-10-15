from sqlalchemy import create_engine, text


class SubjectTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_all(self):
        with self.db.connect() as conn:
        result = conn.execute(text("SELECT * FROM subject WHERE deleted_at IS NULL"))
        return result.mappings().all()

    def create(self, title):
        with self.db.connect() as conn:
            conn.execute(text('INSERT INTO subject("subject_title") VALUES (:title)'), {"title": title})
        conn.commit()

    def update(self, subject_id, new_title):
        with self.db.connect() as conn:
            conn.execute(text('UPDATE subject SET subject_title = :title WHERE subject_id = :subject_id'), {"title": new_title, "subject_id": subject_id})
            conn.commit()

    def delete(self, id):
        with self.db.connect() as conn:
            conn.execute(text('DELETE FROM subject WHERE subject_id = :subject_id'), {"subject_id": subject_id})
            conn.commit()



