from rest_framework.exceptions import APIException
from django.conf import settings

from api.apis import XASession


def xa_login():
    xa_session = XASession()
    response = xa_session.login(
        settings.USERID,
        settings.PASSWORD,
        settings.PASSWORD_CERTIFICATE,
    )

    if not response:
        raise APIException('Failed to login')

    return xa_session