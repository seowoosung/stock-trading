import logging
import win32com.client

from rest_framework.exceptions import APIException
from django.conf import settings

from .api_base import EventHandler

logger = logging.getLogger('quotalogger')


class XAQueryEventHandler(EventHandler):
    def connect(self, xa_query):
        self.xa_query = xa_query
    
    def OnReceiveData(self, tr_code):
        """
        이베스트 서버에서 ReceiveData 이벤트 받으면 실행되는 event handler
        """
        logger.info('OnReceiveData: tr_code[{}]'.format(tr_code))
        self.is_handled = True
        self.xa_query.tr_code = tr_code


class XAQuery:
    def __init__(self):
        self.com_obj = win32com.client.Dispatch("XA_DataSet.XAQuery")
        self.event_handler = win32com.client.WithEvents(self.com_obj, XAQueryEventHandler)
        self.event_handler.connect(self)

        self.name = ''
        self.price = 0
        self.volume = 0
        self.tr_code = None

    def get_single_data(self, stock_code):
        self.com_obj.ResFileName = '{}{}'.format(settings.RES_DIRECTORY, 't1101.res') # RES 파일 등록
        self.com_obj.SetFieldData("t1101InBlock", "shcode", 0, stock_code) # 종목코드 설정
        err_code = self.com_obj.Request(False) # data 요청하기 -- 연속조회인경우만 True

        if err_code < 0:
            raise APIException("Exception: {}".format(err_code))

        self.event_handler.wait()
        
        return {
            'name': self.com_obj.GetFieldData("t1101OutBlock", "hname", 0),
            'price': self.com_obj.GetFieldData("t1101OutBlock", "price", 0),
            'volume': self.com_obj.GetFieldData("t1101OutBlock", "volume", 0),
        }