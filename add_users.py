from data.users import User
from data import db_session

db_session.global_init("db/mars.db")

user = User()
user.name = "Ivan"
user.surname = "Chugunov"
user.email = "vanya@email.ru"
user.age = "17"
user.position = "modul 1"
user.speciality = "sis. admin"
user.address = "Vurnary"
user.password = "fffffff"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
