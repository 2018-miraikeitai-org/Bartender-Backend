from rest_framework_jwt.utils import jwt_payload_handler as default_jwt_payload_handler
from rest_framework import exceptions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# import random
# import string

'''
def jwt_payload_handler(user):
    payload = default_jwt_payload_handler(user)

    payload.pop('user_id')
    payload.pop('email')

    payload['userkey'] = user.jwt.key
    return payload


class JWTAuthentication(JSONWebTokenAuthentication):
    def authenticate_credentials(self, payload):
        user = super(JSONWebTokenAuthentication, self).authenticate_credentials(payload)

        if user.jwt.key != payload.get('userkey'):
            raise exceptions.AuthenticationFailed

        return user
'''
'''
class AuthInfoLogoutView():
    n = random.randint(100, 200)

    def post(self, user, n):
        user.jwt.key = [random.choice(string.ascii_letters + string.digits) for i in range(n)]

        return user
'''