from inputValues import inputField, inputName

def read(db):
    cats = db.cats.find()
    return cats


def readByName(db):
    name = inputName()
    cat = db.cats.find_one({"name": name})
    return cat
