# rb-payment-client


## Getting started

***1. Install the lib***
>pip install git+ssh://git@gitlab.renewbuy.in/consulting/rb-payment-client.git

***2. Set the enviouments variables***
>import os
>
>os.environ["RB_PAYMENT_SECRET_KEY"] = "your_secret_key"
>
>os.environ["RB_PAYMENT_ACCESS_KEY"] = "your_access_key"
>
>os.environ["RB_PAYMENT_JWT_KEY"] = "your_jwt_key"
>
>os.environ["RB_PAYMENT_ENV_TYPE"] = "DEV" # PROD in case of production

***3. Code***
code for getting payment url 
>from rb_payment.client import PaymentHelper
>
>response_data = PaymentHelper.get_payment_url(
>    order_id = 5, 
>    amount= 11000
>)
>
>print(response_data)

reponse
>{
>    "payment_link": "payment-link",
>    "id: "payment identifier id"
>}