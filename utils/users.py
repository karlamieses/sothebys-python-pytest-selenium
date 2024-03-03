users = [
    {"name": "invalid_user", "email": "invalid_format", "password": "my_pass", "first_name": "testName",
     "last_name": "testSurname"},
    {"name": "valid_user", "email": "karlamieses.km@gmail.com", "password": "none__123", "first_name": "testName",
     "last_name": "testSurname"},
]


def get_user(name):
    return next(user for user in users if user["name"] == name)
