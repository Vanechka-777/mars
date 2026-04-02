from data.users import User
from data import db_session

db_session.global_init("db/mars.db")


captain = User()
captain.surname = "Scott"
captain.name = "Ridley"
captain.age = 21
captain.position = "captain"
captain.speciality = "research engineer"
captain.address = "module_1"
captain.email = "scott_chief@mars.org"
captain.password = "captain123"
db_sess = db_session.create_session()
db_sess.add(captain)
db_sess.commit()


colonist1 = User()
colonist1.surname = "Ivanov"
colonist1.name = "Petr"
colonist1.age = 28
colonist1.position = "engineer"
colonist1.speciality = "mechanic"
colonist1.address = "module_2"
colonist1.email = "ivanov@mars.org"
colonist1.password = "ivanov123"
db_sess.add(colonist1)
db_sess.commit()

colonist2 = User()
colonist2.surname = "Kuznetsova"
colonist2.name = "Elena"
colonist2.age = 25
colonist2.position = "doctor"
colonist2.speciality = "therapist"
colonist2.address = "module_3"
colonist2.email = "kuznetsova@mars.org"
colonist2.password = "kuznetsova123"
db_sess.add(colonist2)
db_sess.commit()

colonist3 = User()
colonist3.surname = "Volkov"
colonist3.name = "Alexey"
colonist3.age = 32
colonist3.position = "scientist"
colonist3.speciality = "astrobiologist"
colonist3.address = "module_1"
colonist3.email = "volkov@mars.org"
colonist3.password = "volkov123"
db_sess.add(colonist3)
db_sess.commit()
