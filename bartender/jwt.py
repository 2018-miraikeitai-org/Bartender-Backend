from rest_framework_jwt.utils import jwt_payload_handler as default_jwt_payload_handler
from rest_framework import exceptions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


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

        # user.jwt.keyの変更
        else:
            user.jwt.key = 0

        return user
