import logging
import pythoncom
import time

from django.conf import settings
from rest_framework.exceptions import APIException

logger = logging.getLogger('quotalogger')


class XAComm:
    def __enter__(self):
        # 서브 스레드에서 COM 객체를 사용하려면 COM 라이브러리를 초기화 해야함
        pythoncom.CoInitialize()
    def __exit__(self, e_type, e_value, tb):
        # 사용 후 uninitialize
        pythoncom.CoUninitialize()


class EventHandler:
    def __init__(self):
        self.is_handled = False
    
    def wait(self, timeout=int(settings.EVENT_WAIT_TIMEOUT)):
        start = time.time()
        while not self.is_handled:
            if (time.time() - start) > timeout:
                logger.error('Timeout error while waiting server event')

                raise APIException('Timeout error')
            
            pythoncom.PumpWaitingMessages()