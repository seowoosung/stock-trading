import logging
import win32com.client

from .api_base import EventHandler

logger = logging.getLogger('quotalogger')


class XASessionEventHandler(EventHandler):
    def connect(self, session):
        self.session = session

    def OnLogin(self, code, msg):
        logger.info('OnLogin: code[{}], msg[{}]'.format(code, msg))
        self.is_handled = True
        if code == "0000": # 로그인 성공
            self.session.is_authenticated = True
        else:
            self.session.is_authenticated = False


class XASession:
    def __init__(self):
        self.com_obj = win32com.client.Dispatch("XA_Session.XASession")
        self.event_handler = win32com.client.WithEvents(self.com_obj, XASessionEventHandler)
        self.event_handler.connect(self)

        self.com_obj.ConnectServer("hts.ebestsec.co.kr", 20001)
        
        self.is_authenticated = False

    def login(self, id, passwd, cert):
        self.com_obj.Login(id, passwd, cert, 0, False)
        self.event_handler.wait()
        if self.is_authenticated:
            return True
            
        return False

    def get_account_list(self):
        account_list = []
        for i in range(self.com_obj.GetAccountListCount()):
            account = self.com_obj.GetAccountList(i)
            account_list.append({'account_number': account})

        return account_list