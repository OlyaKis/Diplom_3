import random
import string

DEFAULT_TEST_USER_NAME = "TestUser"


class TestUser:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    @staticmethod
    def generate():
        return TestUser(
            email=generate_email(),
            password=generate_password(),
            name=DEFAULT_TEST_USER_NAME
        )


def generate_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@mail.com"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
