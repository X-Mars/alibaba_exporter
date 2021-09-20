from base import Aliyun
import json, datetime
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest

class Ecs(Aliyun):

    def __init__(self):
        super(Ecs, self).__init__()
        self.metrics_list = []
        self.region_id_list = ['cn-qingdao', 'cn-hongkong']

    def get_expired_ecs_count(self):
        expired_ecs_count = 0
        for region_id in self.region_id_list:
            self.region_id = region_id
            self.make_clt()
            request = DescribeInstancesRequest.DescribeInstancesRequest()
            request.set_accept_format("JSON")
            result = self.clt.do_action_with_exception(request)
            if result:
                result = json.loads(result)

                for instance_info in result['Instances']['Instance']:
                    expired_time = instance_info['ExpiredTime']
                    beijing_expired_time_date = (datetime.datetime.strptime(expired_time, '%Y-%m-%dT%H:%MZ') + datetime.timedelta(hours=8)).date()
                    today = datetime.date.today()
                    expired_days = (beijing_expired_time_date - today).days
                    if expired_days < 10:
                        expired_ecs_count += 1

        info = 'aliyun_expired_ecs_count ' + str(expired_ecs_count)
        print(info)
        self.metrics_list.append(info)

    def get_metrics_list(self):
        self.get_expired_ecs_count()
        return self.metrics_list