from faker import Faker

from random import randint

from inputValues import inputField
from delete import delete_all

def create(db):
    [name, age, features] = inputField()
    return db.cats.insert_one({"name": name, "age": age, "features": features})

def initialize_db(db):
    delete_all(db)
    faker = Faker()
    for _ in range(0, 10):
        features = []
        max_features = randint(0, 5)
        if max_features:
            for i in range(max_features):
                features.append(faker.word())
        db.cats.insert_one({"name": faker.name(), "age": randint(1, 10), "features": features})
    print("Initializing was successful!")
