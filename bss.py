from base import Aliyun
import json
from aliyunsdkbssopenapi.request.v20171214 import QueryAccountBalanceRequest

class Bss(Aliyun):
    
    def __init__(self):
        super(Bss, self).__init__()
        self.metrics_list = []

    def get_aliyun_balance(self):
        balance = 0
        request = QueryAccountBalanceRequest.QueryAccountBalanceRequest()
        request.set_accept_format("JSON")
        result = self.clt.do_action_with_exception(request)
        result = json.loads(result)
        if result['Code'] == '200':
            balance = result['Data']['AvailableCashAmount']

        info = 'aliyun_balance ' + str(balance)
        print(info)
        self.metrics_list.append(info)

    def get_metrics_list(self):
        self.get_aliyun_balance()
        return self.metrics_list