import os
env_type = os.environ.get("RB_PAYMENT_ENV_TYPE")

BASE_URL = "https://payment.rbstaging.in/"
if env_type == "PROD":
    base_url = "https://payment.renewbuyfinsure.com/"