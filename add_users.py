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

user = User()
user.name = "Maks"
user.surname = "Charkov"
user.email = "maks@email.ru"
user.age = "19"
user.position = "modul 2"
user.speciality = "mechanic"
user.address = "Moskow"
user.password = "maks123"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Petya"
user.surname = "Stepanov"
user.email = "petya@email.ru"
user.age = "21"
user.position = "modul 3"
user.speciality = "builder"
user.address = "St.Petersburg"
user.password = "petya123"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()
