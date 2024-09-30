import requests
from faker import Faker
from data import Urls


class TestDataHelper:
    @staticmethod
    def create_user_data():
        fake = Faker()

        data = {
            "name": fake.name(),
            "email": fake.email(),
            "password": fake.password()
        }

        return data

    @staticmethod
    def delete_user(token):
        response = requests.delete(Urls.INFO_USER, headers={'Authorization': token})

        return response
