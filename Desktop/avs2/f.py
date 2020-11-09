from Managers.DatabaseManager import DatabaseManager
from app import db

db_manager = DatabaseManager(db)
db_manager.add_lecturer(first_name='Гудкова', last_name='Ирина', patronymic='Алексеевна')
db_manager.add_lecturer(first_name='Волков', last_name='Андрей', patronymic='Иванович')
db_manager.add_lecturer(first_name='Гуриков', last_name='Сергей', patronymic='Ростиславович')
db_manager.add_lecturer(first_name='Воробейчиков', last_name='Леонид', patronymic='Александрович')
db_manager.add_lecturer(first_name='Мальцева', last_name='Светлана', patronymic='Николаевна')