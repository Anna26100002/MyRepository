from models.Lecturer import Lecturer


class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def add_lecturer(self, **kwargs):
        lecturer = Lecturer(first_name=kwargs["first_name"],
                            last_name=kwargs["last_name"],
                            patronymic=kwargs["patronymic"]
                            )
        self.db.session.add(lecturer)
        self.db.session.commit()