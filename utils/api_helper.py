from utils.test_data import TestUser
import requests


def create_test_user(user: TestUser):
    return UserAPI.create_user(user.email, user.password, user.name)


def delete_test_user(user: TestUser):
    token_response = UserAPI.login_user(user.email, user.password)
    if token_response.status_code == 200:
        access_token = token_response.json()["accessToken"]
        return UserAPI.delete_user(access_token)
    else:
        return None


def create_order(user: TestUser):
    token_response = UserAPI.login_user(user.email, user.password)
    if token_response.status_code != 200:
        raise Exception("Can't login user for order creation")
    access_token = token_response.json()["accessToken"]
    ingredients_response = requests.get(f"{UserAPI.BASE_URL}/ingredients")
    ingredients = ingredients_response.json()["data"]
    bun = next((i["_id"] for i in ingredients if i["type"] == "bun"), None)
    filling = next((i["_id"] for i in ingredients if i["type"] == "main"), None)
    ingredient_ids = []
    if bun:
        ingredient_ids.append(bun)
    if filling:
        ingredient_ids.append(filling)
    if not ingredient_ids:
        raise Exception("No valid ingredients found")
    headers = {"Authorization": access_token}
    payload = {"ingredients": ingredient_ids}
    response = requests.post(f"{UserAPI.BASE_URL}/orders", json=payload, headers=headers)
    return response


class UserAPI:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    @staticmethod
    def create_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return requests.post(f"{UserAPI.BASE_URL}/auth/register", json=payload)

    @staticmethod
    def delete_user(token):
        headers = {"Authorization": token}
        return requests.delete(f"{UserAPI.BASE_URL}/auth/user", headers=headers)

    @staticmethod
    def login_user(email, password):
        payload = {
            "email": email,
            "password": password
        }
        return requests.post(f"{UserAPI.BASE_URL}/auth/login", json=payload)
