import re

from mitsubishi_central_controller.util.constants import DRIVE_STRINGS, MODE_MAP, AIR_DIRECTION_MAP, FAN_SPEED_MAP, \
    REMOTE_CONTROL_PERMISSION_MAP, ITEM_MAP, VENTILATION_MAP, SIGN_MAP, MODEL_MAP, STATUS_MAP, SCHEDULE_MAP, \
    IC_KIND_MAP, FAN_SPEED_STATUS_MAP, AIR_STAGE_STATUS_MAP


def bulk_string_to_list_of_hex(bulk_string):
    return re.findall('..', bulk_string)


def extract_drive(list_of_hex):
    drive = int(list_of_hex[1], 16)
    drive_string = DRIVE_STRINGS[drive]
    return drive_string


def extract_mode(list_of_hex):
    mode = int(list_of_hex[2], 16)
    mode_string = MODE_MAP[mode]
    return mode_string


def extract_set_temperature(list_of_hex):
    left = int(list_of_hex[3], 16)
    right = int(list_of_hex[4], 16)
    if right <= 0 or right >= 10:
        return str(left)
    else:
        return str(left) + "." + str(right)


def extract_inlet_temperature(list_of_hex):
    number = int(list_of_hex[5] + list_of_hex[6], 16)
    float_number = float(number) / 10.0
    return str(float_number)


def extract_air_direction(list_of_hex):
    air_direction = int(list_of_hex[7], 16)
    air_direction_string = AIR_DIRECTION_MAP[air_direction]
    return air_direction_string


def extract_fan_speed(list_of_hex):
    fan_speed = int(list_of_hex[8], 16)
    fan_speed_string = FAN_SPEED_MAP[fan_speed]
    return fan_speed_string


def extract_remote_control_permission(list_of_hex):
    remote_control_permission = int(list_of_hex[9], 16)
    remote_control_permission_string = REMOTE_CONTROL_PERMISSION_MAP[remote_control_permission]
    return remote_control_permission_string


def extract_drive_item(list_of_hex):
    drive_item = int(list_of_hex[10], 16)
    drive_item_string = ITEM_MAP[drive_item]
    return drive_item_string


def extract_mode_item(list_of_hex):
    mode_item = int(list_of_hex[11], 16)
    mode_item_string = ITEM_MAP[mode_item]
    return mode_item_string


def extract_set_temperature_item(list_of_hex):
    set_temperature_item = int(list_of_hex[12], 16)
    set_temperature_item_string = ITEM_MAP[set_temperature_item]
    return set_temperature_item_string


def extract_filter_item(list_of_hex):
    filter_item = int(list_of_hex[13], 16)
    filter_item_string = ITEM_MAP[filter_item]
    return filter_item_string


def extract_ventilation(list_of_hex):
    ventilation = int(list_of_hex[14], 16)
    ventilation_string = VENTILATION_MAP[ventilation]
    return ventilation_string


def extract_filter_sign(list_of_hex):
    filter_sign = int(list_of_hex[15], 16)
    filter_sign_string = SIGN_MAP[filter_sign]
    return filter_sign_string


def extract_error_sign(list_of_hex):
    error_sign = int(list_of_hex[16], 16)
    error_sign_string = SIGN_MAP[error_sign]
    return error_sign_string


def extract_model(list_of_hex):
    model = int(list_of_hex[17], 16)
    model_string = MODEL_MAP[model]
    return model_string


def extract_mode_status(list_of_hex):
    mode_status = int(list_of_hex[18], 16)
    mode_status_string = STATUS_MAP[mode_status]
    return mode_status_string


def extract_mid_temp_status(list_of_hex):
    mid_temp_status = int(list_of_hex[19], 16)
    mid_temp_status_string = STATUS_MAP[mid_temp_status]
    return mid_temp_status_string


def extract_maximum_save_value(list_of_hex):
    maximum_save_value = int(list_of_hex[20], 16)
    if maximum_save_value > 0:
        return "100"
    else:
        return "0"


def extract_schedule(list_of_hex):
    schedule = int(list_of_hex[21], 16)
    schedule_string = SCHEDULE_MAP[schedule]
    return schedule_string


def extract_ic_kind(list_of_hex):
    ic_kind = int(list_of_hex[22], 16)
    ic_kind_string = IC_KIND_MAP[ic_kind]
    return ic_kind_string


def extract_auto_mode_status(list_of_hex):
    auto_mode_status = int(list_of_hex[23], 16)
    auto_mode_status_string = STATUS_MAP[auto_mode_status]
    return auto_mode_status_string


def extract_dry_mode_status(list_of_hex):
    dry_mode_status = int(list_of_hex[24], 16)
    return STATUS_MAP[dry_mode_status]


def extract_fan_speed_status(list_of_hex):
    fan_speed_status = int(list_of_hex[25], 16)
    return FAN_SPEED_STATUS_MAP[fan_speed_status]


def extract_air_direction_status(list_of_hex):
    air_direction_status = int(list_of_hex[26], 16)
    return STATUS_MAP[air_direction_status]


def extract_swing_status(list_of_hex):
    swing_status = int(list_of_hex[27], 16)
    return STATUS_MAP[swing_status]


def extract_ventilation_status(list_of_hex):
    ventilation_status = int(list_of_hex[28], 16)
    return STATUS_MAP[ventilation_status]


def extract_bypass_status(list_of_hex):
    bypass_status = int(list_of_hex[29], 16)
    return STATUS_MAP[bypass_status]


def extract_lc_auto_status(list_of_hex):
    lc_auto_status = int(list_of_hex[30], 16)
    return STATUS_MAP[lc_auto_status]


def extract_heat_recovery_status(list_of_hex):
    heat_recovery_status = int(list_of_hex[31], 16)
    return STATUS_MAP[heat_recovery_status]


def _change_limit_min_max(a: int, b: int):
    return str(int(a[0], 16)) + str(int(a[1], 16)) + "." + str(int(b, 16))


def extract_cool_min(list_of_hex):
    a = list_of_hex[32]
    b = list_of_hex[38][0]
    return _change_limit_min_max(a, b)


def extract_cool_max(list_of_hex):
    a = list_of_hex[34]
    b = list_of_hex[39][0]
    return _change_limit_min_max(a, b)


def extract_heat_min(list_of_hex):
    a = list_of_hex[35]
    b = list_of_hex[39][1]
    return _change_limit_min_max(a, b)


def extract_heat_max(list_of_hex):
    a = list_of_hex[33]
    b = list_of_hex[38][1]
    return _change_limit_min_max(a, b)


def extract_auto_min(list_of_hex):
    a = list_of_hex[36]
    b = list_of_hex[40][0]
    return _change_limit_min_max(a, b)


def extract_auto_max(list_of_hex):
    a = list_of_hex[37]
    b = list_of_hex[40][1]
    return _change_limit_min_max(a, b)


def extract_turn_off(list_of_hex):
    i = int(list_of_hex[41], 16)
    return SCHEDULE_MAP[i]


def extract_temp_limit(list_of_hex):
    temp_limit = int(list_of_hex[42], 16)
    return STATUS_MAP[temp_limit]


def extract_temp_detail(list_of_hex):
    temp_detail = int(list_of_hex[43], 16)
    return STATUS_MAP[temp_detail]


def extract_fan_mode_status(list_of_hex):
    fan_mode = int(list_of_hex[44], 16)
    return STATUS_MAP[fan_mode]


def extract_air_stage_status(list_of_hex):
    air_stage_status = int(list_of_hex[45], 16)
    return AIR_STAGE_STATUS_MAP[air_stage_status]


def extract_air_auto_status(list_of_hex):
    air_auto_status = int(list_of_hex[46], 16)
    return STATUS_MAP[air_auto_status]


def extract_fan_auto_status(list_of_hex):
    fan_auto_status = int(list_of_hex[47], 16)
    return STATUS_MAP[fan_auto_status]
