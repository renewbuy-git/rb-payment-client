import requests
import os

from .jwt_helper import JWT
from .constants import BASE_URL



secret_key = os.environ.get("RB_PAYMENT_SECRET_KEY")
jwt_key = os.environ.get("RB_PAYMENT_JWT_KEY")
access_key = os.environ.get("RB_PAYMENT_ACCESS_KEY")


class PaymentHelper:
    @staticmethod
    def get_payment_url(order_id:int, amount: float):
        dict_data = {
            "order_id": order_id,
            "amount": amount,
        }
        encoded_jwt_data = {"data":JWT.encode(dict_data, jwt_key)}

        header = {
            "Secret-Key" : secret_key,
            "Access-Key" : access_key
        }

        responce = requests.post(
            f"{BASE_URL}api/v1/pay/get_payment_link/",
            json= encoded_jwt_data,
            headers = header
        )

        return responce.json()
