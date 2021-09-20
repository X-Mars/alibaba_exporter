from base import Aliyun
import json, datetime
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest

class Rds(Aliyun):

    def __init__(self):
        super(Rds, self).__init__()
        self.metrics_list = []
        self.region_id_list = ['cn-qingdao', 'cn-hongkong']

    def get_aliyun_rds(self):
        expired_rds_count = 0
        for region_id in self.region_id_list:
            self.region_id = region_id
            self.make_clt()
            request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
            request.set_accept_format("JSON")
            result = self.clt.do_action_with_exception(request)
            if result:
                result = json.loads(result)

                for instance_info in result['Items']['DBInstance']:
                    expired_time = instance_info['ExpireTime']
                    beijing_expired_time_date = (
                                datetime.datetime.strptime(expired_time, '%Y-%m-%dT%H:%M:%SZ') + datetime.timedelta(
                            hours=8)).date()
                    today = datetime.date.today()
                    expired_days = (beijing_expired_time_date - today).days
                    if expired_days < 10:
                        expired_rds_count += 1

        info = 'aliyun_expired_rds_count ' + str(expired_rds_count)
        print(info)
        self.metrics_list.append(info)

    def get_metrics_list(self):
        self.get_aliyun_rds()
        return self.metrics_list