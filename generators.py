import random
import secrets
import string


def generate_email():
    adjectives = [
        "adorable",
        "adventurous",
        "aggressive",
        "agreeable",
        "alert",
        "alive",
        "amused",
        "angry",
        "annoyed",
        "annoying",
        "anxious",
        "arrogant",
        "ashamed",
        "attractive",
        "average",
    ]
    nouns = [
        "human",
        "dog",
        "way",
        "art",
        "world",
        "information",
        "map",
        "family",
        "government",
        "health",
    ]
    return f"{random.choice(adjectives)}_{random.choice(nouns)}_{random.randint(0, 100)}@gmail.com"


def generate_phone():
    numbers = "".join([str(random.randint(1, 9)) for _ in range(6)])
    return "3125" + numbers


def generate_first_name():
    options = [
        "James",
        "Robert",
        "John",
        "Michael",
        "David",
        "William",
        "Richard",
        "Joseph",
        "Thomas",
        "Christopher",
    ]
    return random.choice(options)


def generate_last_name():
    options = [
        "Smith",
        "Johnson",
        "Brown",
        "Jones",
        "Garcia",
        "Miler",
        "Davis",
        "Rodriguez",
        "Martinez",
    ]
    return random.choice(options)


def generate_password():
    symbols = string.ascii_letters + string.digits + string.punctuation
    return "".join([secrets.choice(symbols) for _ in range(10)])


def generate_birt_date():
    options = [
        "02161980",
        "08251975",
        "10051986",
        "11291990",
    ]
    return random.choice(options)
