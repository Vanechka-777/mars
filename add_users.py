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

colonists = [
    {
        'surname': 'Ivanov',
        'name': 'Petr',
        'age': 28,
        'position': 'engineer',
        'speciality': 'mechanic',
        'address': 'module_2',
        'email': 'ivanov@mars.org',
        'password': 'ivanov123'
    },
    {
        'surname': 'Kuznetsova',
        'name': 'Elena',
        'age': 25,
        'position': 'doctor',
        'speciality': 'therapist',
        'address': 'module_3',
        'email': 'kuznetsova@mars.org',
        'password': 'kuznetsova123'
    },
    {
        'surname': 'Volkov',
        'name': 'Alexey',
        'age': 32,
        'position': 'scientist',
        'speciality': 'astrobiologist',
        'address': 'module_1',
        'email': 'volkov@mars.org',
        'password': 'volkov123'
    }
]