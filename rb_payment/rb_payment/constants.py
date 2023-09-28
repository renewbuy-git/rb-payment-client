import os
env_type = os.environ.get("RB_PAYMENT_ENV_TYPE")

if env_type == "PROD":
    base_url = "https://rb-payment.herokuapp.com"