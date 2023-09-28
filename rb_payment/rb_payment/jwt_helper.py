import datetime
import jwt

class JWT:
    """
    Class for encoding and decoding JWT.
    """

    @staticmethod
    def encode(payload:dict, secret_key:str, exp_hr:int=0, algorithm="HS256"):
        """
        Encodes the payload into a JWT.

        Args:
            payload (dict): The payload to be encoded.
            secret_key (str): The secret key used for encoding.
            algorithm (str): The algorithm used for encoding.

        Returns:
            str: The encoded JWT.
        """
        if exp_hr > 0:  # If expiration time is set, update the payload with the expiration time.
            payload.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(hours=exp_hr)})  # Expiration time
        return jwt.encode(payload, secret_key, algorithm=algorithm)

    @staticmethod
    def decode(encoded_jwt, secret_key, algorithms=["HS256"]):
        """
        Decodes the JWT into a payload.

        Args:
            encoded_jwt (str): The encoded JWT.
            secret_key (str): The secret key used for decoding.
            algorithms (list): The algorithms used for decoding.

        Returns:
            dict: The decoded payload.
        """
        try:
            return True, jwt.decode(encoded_jwt, secret_key, algorithms=algorithms)
        except jwt.ExpiredSignatureError:
            return False, "Token has expired."
        except jwt.InvalidTokenError:
            return False, "Invalid token."