from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings
from .serializers import OrdinaryUserSerializer

def jwt_response_payload_handler(token, user=None, unused_request=None):
    context = OrdinaryUserSerializer(user.baseuser).data
    context['token'] = token

    return context


def get_token(user):
    payload = api_settings.JWT_PAYLOAD_HANDLER(user)
    token = api_settings.JWT_ENCODE_HANDLER(payload)

    return token


def authenticate_user(user):
    django_client = APIClient()

    user_token = get_token(user)
    token = 'JWT {}'.format(user_token)

    django_client.credentials(HTTP_AUTHORIZATION=token)

    return django_client
