from faker import Faker
from random import randrange

def data_samples():
    fk = Faker('ru_RU')
    return [[fk.name(), fk.phone_number(), randrange(0,100), randrange(0,100)] for _ in range(20)]
