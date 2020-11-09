from Managers.DBM2 import DatabaseManager
from app import db

db_manager = DatabaseManager(db)
db_manager.add_interval(time='9:30-11:05')
db_manager.add_interval(time='11:20-12:55')
db_manager.add_interval(time='13:10-14:45')
db_manager.add_interval(time='15:25-17:00')
db_manager.add_interval(time='17:15-18:50')

