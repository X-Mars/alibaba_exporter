from aliyunsdkcore.client import AcsClient

class Aliyun():

    def __init__(self):
        self.apikey = ''
        self.secret = ''
        self.region_id = 'cn-qingdao'
        self.make_clt()

    def make_clt(self):
        self.clt = AcsClient(self.apikey, self.secret, self.region_id)

