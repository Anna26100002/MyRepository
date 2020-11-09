from models.Interval import Interval


class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def add_interval(self, **kwargs):
        interval = Interval(time=kwargs["time"])
        self.db.session.add(interval)
        self.db.session.commit()