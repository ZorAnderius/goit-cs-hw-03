def inputField(update=False):
    change = False
    name = None
    age = None
    features = None
    if update:
        change = isChange("name")
    if not change:
        name = inputName()

    if update:
        change = isChange("age")
    if not change:
        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                print("Invalid age")
    if update:
        change = isChange("all features")
    if not change:
        features = []
    while True and not change:
        feature = str(input("Enter features('exit' for exit): "))
        if feature == "exit":
            break
        if feature == "":
            print("Feature can't be empty. Try again or 'exit' to exit.")
            continue
        features.append(feature)
    return (name, age, features)


def inputID():
    while True:
        id = str(input("Enter id: "))
        if id == "exit":
            return None
        if id and len(id) == 24 and all(c in "0123456789abcdef" for c in id):
            return id
        print("Invalid input. ID must has 24 characters length.Try again or 'exit' to exit")


def inputName():
    while True:
        name = str(input("Enter name: "))
        if name:
            return name
        print("Invalid input")

def isChange(title):
    while True:
        change = str(input(f"Change {title} Y/N: "))
        if change:
            change = change.lower()
            if change == "y":
                return False
            elif change == "n":
                return True
        print("Wrong input. Try again or 'exit' to exit")
