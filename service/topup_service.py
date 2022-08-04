from entity.duration_unit import DurationUnit
from entity.topup import Topup


class TopupService:
    One_Month_Duration_Unit = 1
    Four_Device_Count = 4
    Ten_Device_Count = 10

    Four_Device_Cost = 50
    Ten_Device_Cost = 100

    Four_Device_Plan_Name = "FOUR_DEVICE"
    Ten_Device_Plan_Name = "TEN_DEVICE"

    def __init__(self):
        self.topup_plan_type = {}
        self.__preload_data()

    def __preload_data(self):
        four_device_topup = Topup(TopupService.Four_Device_Plan_Name, TopupService.Four_Device_Count,DurationUnit.MONTH,
                                 TopupService.One_Month_Duration_Unit,
                                 TopupService.Four_Device_Cost)

        ten_device_topup = Topup(TopupService.Ten_Device_Plan_Name, TopupService.Ten_Device_Count,DurationUnit.MONTH,
                                  TopupService.One_Month_Duration_Unit,
                                  TopupService.Ten_Device_Cost)

        self.topup_plan_type[TopupService.Four_Device_Plan_Name] = four_device_topup
        self.topup_plan_type[TopupService.Ten_Device_Plan_Name] = ten_device_topup

    def get_topup_plan(self):
        return self.topup_plan_type
