from mitsubishi_central_controller.util.xml_utils import build_xml


class ControllerDictBuilder:
    def __init__(self):
        self.dict = {
            "Command": "",
            "DatabaseManager": {
                "ControlGroup": {}
            }
        }

    def get_mnet_group_list(self):
        self.dict["Command"] = "getRequest"
        self.dict["DatabaseManager"] = {
            "ControlGroup": {
                "MnetGroupList": {}
            }
        }
        return self

    def get_system_data(self):
        self.dict["Command"] = "getRequest"
        self.dict["DatabaseManager"] = {
            "SystemData": {
                "@Version": "*",
                "@TempUnit": "*",
                "@Model": "*",
                "@FilterSign": "*",
                "@ShortName": "*",
                "@DateFormat": "*"
            }
        }
        return self

    def get_single_bulk_data(self, group_id):
        self.dict["Command"] = "getRequest"
        self.dict["DatabaseManager"] = {
            "Mnet": {
                "@Group": group_id,
                "@Bulk": "*",
                "@EnergyControl": "*",
                "@RacSW": "*"
            }
        }
        return self

    def get_mnet_list(self):
        self.dict["Command"] = "getRequest"
        self.dict["DatabaseManager"] = {
            "ControlGroup": {
                "MnetList": {}
            }
        }
        return self

    def get_mnet(self, group, lcd_name=False):
        self.dict["Command"] = "getRequest"
        self.dict["DatabaseManager"] = {
            "Mnet": {
                "@Group": str(group)
            }
        }
        if lcd_name:
            self.dict["DatabaseManager"]["Mnet"]["@GroupNameLcd"] = "*"
        return self

    def set_mnet(self, group, drive=None, mode=None, set_temp=None, air_direction=None, fan_speed=None,
                 remote_controller=None,
                 error_sign=None, filter_sign=None):
        self.dict["Command"] = "setRequest"
        self.dict["DatabaseManager"] = {
            "Mnet": {
                "@Group": str(group)
            }
        }

        if drive is not None:
            self.dict["DatabaseManager"]["Mnet"]["@Drive"] = drive
        if mode is not None:
            self.dict["DatabaseManager"]["Mnet"]["@Mode"] = mode
        if set_temp is not None:
            self.dict["DatabaseManager"]["Mnet"]["@SetTemp"] = set_temp
        if air_direction is not None:
            self.dict["DatabaseManager"]["Mnet"]["@AirDirection"] = air_direction
        if fan_speed is not None:
            self.dict["DatabaseManager"]["Mnet"]["@FanSpeed"] = fan_speed
        if remote_controller is not None:
            self.dict["DatabaseManager"]["Mnet"]["@RemoCon"] = remote_controller
        if error_sign is not None:
            self.dict["DatabaseManager"]["Mnet"]["@ErrorSign"] = error_sign
        if filter_sign is not None:
            self.dict["DatabaseManager"]["Mnet"]["@FilterSign"] = filter_sign

        return self

    def to_xml(self):
        return build_xml(self.dict)
