import mitsubishi_central_controller.util.bulk as bulk
from mitsubishi_central_controller.util.ControllerDictBuilder import ControllerDictBuilder
from mitsubishi_central_controller.util.temperature_utils import c_to_f
from mitsubishi_central_controller.util.xml_utils import parse_xml


class Group:
    def __init__(self, group_id, model_code, address):
        self.group_id = group_id
        self.model_code = model_code
        self.address = address
        self.bulk_string = None
        self.rac_sw = None
        self.energy_control = None
        self.current_drive = None
        self.current_set_temperature = None
        self.current_inlet_temperature = None
        self.current_mode = None
        self.current_air_direction = None
        self.current_fan_speed = None
        self.current_remote_control_permission = None
        self.current_drive_item = None
        self.current_mode_item = None
        self.current_set_temperature_item = None
        self.current_filter_item = None
        self.current_ventilation = None
        self.current_filter_sign = None
        self.current_error_sign = None
        self.current_model = None
        self.current_mode_status = None
        self.current_mid_temp_status = None
        self.current_maximum_save_value = None
        self.current_schedule = None
        self.current_ic_kind = None
        self.current_auto_mode_status = None
        self.current_dry_mode_status = None
        self.current_fan_speed_status = None
        self.current_air_direction_status = None
        self.current_swing_status = None
        self.current_ventilation_status = None
        self.current_bypass_status = None
        self.current_lc_auto_status = None
        self.current_heat_recovery_status = None
        self.current_cool_min = None
        self.current_cool_max = None
        self.current_heat_min = None
        self.current_heat_max = None
        self.current_auto_min = None
        self.current_auto_max = None
        self.current_turn_off = None
        self.current_temp_limit = None
        self.current_temp_detail = None
        self.current_fan_mode_status = None
        self.current_air_stage_status = None
        self.current_air_auto_status = None
        self.current_fan_auto_status = None
        self.current_set_temperature_fahrenheit = None
        self.current_inlet_temperature_fahrenheit = None
        self.lcd_name = None
        self.web_name = None
        self.available_fan_speeds = None
        self.available_air_directions = None



    def update_from_bulk(self):
        if self.bulk_string is None:
            raise AssertionError("You must populate the bulk string before parsing it!")
        list_of_hex = bulk.bulk_string_to_list_of_hex(self.bulk_string)
        self.current_drive = bulk.extract_drive(list_of_hex)
        self.current_mode = bulk.extract_mode(list_of_hex)
        self.current_set_temperature = bulk.extract_set_temperature(list_of_hex)
        self.current_inlet_temperature = bulk.extract_inlet_temperature(list_of_hex)
        self.current_air_direction = bulk.extract_air_direction(list_of_hex)
        self.current_fan_speed = bulk.extract_fan_speed(list_of_hex)
        self.current_remote_control_permission = bulk.extract_remote_control_permission(list_of_hex)
        self.current_drive_item = bulk.extract_drive_item(list_of_hex)
        self.current_mode_item = bulk.extract_mode_item(list_of_hex)
        self.current_set_temperature_item = bulk.extract_set_temperature_item(list_of_hex)
        self.current_filter_item = bulk.extract_filter_item(list_of_hex)
        self.current_ventilation = bulk.extract_ventilation(list_of_hex)
        self.current_filter_sign = bulk.extract_filter_sign(list_of_hex)
        self.current_error_sign = bulk.extract_error_sign(list_of_hex)
        self.current_model = bulk.extract_model(list_of_hex)
        self.current_mode_status = bulk.extract_mode_status(list_of_hex)
        self.current_mid_temp_status = bulk.extract_mid_temp_status(list_of_hex)
        self.current_maximum_save_value = bulk.extract_maximum_save_value(list_of_hex)
        self.current_schedule = bulk.extract_schedule(list_of_hex)
        self.current_ic_kind = bulk.extract_ic_kind(list_of_hex)
        self.current_auto_mode_status = bulk.extract_auto_mode_status(list_of_hex)
        self.current_dry_mode_status = bulk.extract_dry_mode_status(list_of_hex)
        self.current_fan_speed_status = bulk.extract_fan_speed_status(list_of_hex)
        self.current_air_direction_status = bulk.extract_air_direction_status(list_of_hex)
        self.current_swing_status = bulk.extract_swing_status(list_of_hex)
        self.current_ventilation_status = bulk.extract_ventilation_status(list_of_hex)
        self.current_bypass_status = bulk.extract_bypass_status(list_of_hex)
        self.current_lc_auto_status = bulk.extract_lc_auto_status(list_of_hex)
        self.current_heat_recovery_status = bulk.extract_heat_recovery_status(list_of_hex)
        self.current_cool_min = bulk.extract_cool_min(list_of_hex)
        self.current_cool_max = bulk.extract_cool_max(list_of_hex)
        self.current_heat_min = bulk.extract_heat_min(list_of_hex)
        self.current_heat_max = bulk.extract_heat_max(list_of_hex)
        self.current_auto_min = bulk.extract_auto_min(list_of_hex)
        self.current_auto_max = bulk.extract_auto_max(list_of_hex)
        self.current_turn_off = bulk.extract_turn_off(list_of_hex)
        self.current_temp_limit = bulk.extract_temp_limit(list_of_hex)
        self.current_temp_detail = bulk.extract_temp_detail(list_of_hex)
        self.current_fan_mode_status = bulk.extract_fan_mode_status(list_of_hex)
        self.current_air_stage_status = bulk.extract_air_stage_status(list_of_hex)
        self.current_air_auto_status = bulk.extract_air_auto_status(list_of_hex)
        self.current_fan_auto_status = bulk.extract_fan_auto_status(list_of_hex)
        self.update_fahrenheit_values()
        self.update_available_air_directions()
        self.update_available_fan_speeds()

    def update_fahrenheit_values(self):
        self.current_set_temperature_fahrenheit = c_to_f(self.current_set_temperature)
        self.current_inlet_temperature_fahrenheit = round((float(self.current_inlet_temperature) * (9 / 5)) + 32, 1)

    def update_available_fan_speeds(self):
        fan_speed_status = self.current_fan_speed_status
        fan_auto_status = self.current_fan_auto_status
        if fan_speed_status == "3STAGES":
            self.available_fan_speeds = ["HIGH", "MID2", "LOW"]
        elif fan_speed_status == "4STAGES":
            self.available_fan_speeds = ["HIGH", "MID2", "MID1", "LOW"]
        else:
            self.available_fan_speeds = ["HIGH", "LOW"]
        if fan_auto_status == "ENABLE":
            self.available_fan_speeds.append("AUTO")

    def update_available_air_directions(self):
        air_stage_status = self.current_air_stage_status
        air_auto_status = self.current_air_auto_status
        swing_status = self.current_swing_status
        if air_stage_status == "5STAGES":
            self.available_air_directions = ["VERTICAL", "MID2", "MID1", "MID0", "HORIZONTAL"]
        else:
            self.available_air_directions = ["VERTICAL", "MID2", "MID1", "HORIZONTAL"]
        if air_auto_status == "ENABLE":
            self.available_air_directions.append("AUTO")
        if swing_status == "ENABLE":
            self.available_air_directions.append("SWING")

    def update_operation_modes(self):
        self.modes = ["COOL", "HEAT"]
        if self.current_fan_mode_status == "ENABLE":
            self.modes.append("FAN")
        if self.current_dry_mode_status == "ENABLE":
            self.modes.append("DRY")