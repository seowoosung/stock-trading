import logging

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import APIException

from api.serializers import AccountResponseSerializer
from api.apis import XAComm
from api.utils import xa_login

logger = logging.getLogger('quotalogger')


class AccountsView(APIView):
    @swagger_auto_schema(
        tags=['api'],
        operation_id='계좌조회',
        responses={
            200: AccountResponseSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        logger.info('계좌조회')

        with XAComm() as xa_comm:
            xa_session = xa_login()
            accounts = xa_session.get_account_list()

        return JsonResponse(AccountResponseSerializer(accounts, many=True).data, safe=False, status=status.HTTP_200_OK)