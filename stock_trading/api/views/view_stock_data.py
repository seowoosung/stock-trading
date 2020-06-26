import logging

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import APIException

from api.serializers import StockDataResponseSerializer
from api.apis import XAComm, XAQuery
from api.utils import xa_login

logger = logging.getLogger('quotalogger')


class StockDataView(APIView):
    @swagger_auto_schema(
        tags=['api'],
        operation_id='종목 조회',
        manual_parameters=[
            openapi.Parameter('stock_code', openapi.IN_QUERY, description='종목코드', type=openapi.TYPE_STRING),
        ],
        responses={
            200: StockDataResponseSerializer(),
        },
    )
    def get(self, request, *args, **kwargs):
        logger.info('종목 조회')

        with XAComm() as xa_comm:
            xa_session = xa_login()
            single_data = XAQuery().get_single_data(stock_code=request.GET.get('stock_code'))

        return JsonResponse(StockDataResponseSerializer(single_data).data, safe=False, status=status.HTTP_200_OK)