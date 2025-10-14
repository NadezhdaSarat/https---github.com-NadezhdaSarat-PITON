from sqlalchemy import create_engine, text


class SubjectTable:
    #db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
    __scripts = {
        "select": text("SELECT * FROM subject WHERE deleted_at IS NULL"),
        "delete by subject_id": text("DELETE FROM company WHERE id =:id_to_delete"),
        "insert_new": text("INSERT INTO subject(\"title\") values (:new_title)"),
        "get_max_subject_id": text("SELECT MAX(\"subject_id\") FROM subject WHERE deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_subject_table(self):
        conn = self.db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_subject_title(self):
        conn = self.db.connect()
        result = conn.execute(
            text("SELECT * FROM subject "
                 "WHERE \"subject_title\" = Russian"
                 "AND deleted_at IS NULL")
        )
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete_by_subject_id"], {"subject_id": id})
        conn.close()

    def create(self, title):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"], {"new_title": title})
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_subject_id"])
        max_id = result.scalar()
        conn.close()
        return max_id




