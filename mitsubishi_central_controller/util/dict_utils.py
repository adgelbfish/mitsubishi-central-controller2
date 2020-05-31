from mitsubishi_central_controller.classes.Group import Group
from mitsubishi_central_controller.classes.SystemData import SystemData


def get_group_list_from_dict(obj):
    return [Group(group_id=group_data["@Group"], model_code=group_data["@Model"], address=group_data["@Address"]) for
            group_data in obj["Packet"]["DatabaseManager"]["ControlGroup"]["MnetGroupList"]["MnetGroupRecord"]]


def get_group_info_list_from_dict(obj):
    groups_info = {}
    for group_data in obj["Packet"]["DatabaseManager"]["ControlGroup"]["MnetList"]["MnetRecord"]:
        groups_info[group_data["@Group"]] = {
            "web_name": group_data["@GroupNameWeb"],
            "lcd_name": group_data["@GroupNameLcd"]
        }
    return groups_info


def get_lcd_name_from_dict(obj):
    return obj["Packet"]["DatabaseManager"]["Mnet"]["@GroupNameLcd"]


def get_web_name_from_dict(obj):
    return obj["Packet"]["DatabaseManager"]["Mnet"]["@GroupNameWeb"]


def get_system_data_from_dict(obj):
    data_obj = obj["Packet"]["DatabaseManager"]["SystemData"]
    return SystemData(version=data_obj["@Version"], temp_unit=data_obj["@TempUnit"], model=data_obj['@Model'],
                      filter_sign=data_obj["@FilterSign"], short_name=data_obj["@ShortName"],
                      date_format=["@DateFormat"])


def get_single_bulk_from_dict(obj):
    data_obj = obj["Packet"]["DatabaseManager"]["Mnet"]
    return data_obj["@Bulk"]


def get_single_racsw_from_dict(obj):
    data_obj = obj["Packet"]["DatabaseManager"]["Mnet"]
    return data_obj["@RacSW"]


def get_single_energycontrol_from_dict(obj):
    data_obj = obj["Packet"]["DatabaseManager"]["Mnet"]
    return data_obj["@EnergyControl"]
