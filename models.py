# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models










class CollectorParams(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    rate = models.BigIntegerField(blank=True, null=True)
    ct = models.IntegerField(blank=True, null=True)
    pt = models.IntegerField(blank=True, null=True)
    lct = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'collector_params'


class CollectorStatus(models.Model):
    device_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collector_status'


class CollectorType(models.Model):
    des = models.CharField(max_length=255, blank=True, null=True)
    des_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collector_type'


class CommandQueue(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    command = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'command_queue'


class Company(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    city_id = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    nav_flag = models.IntegerField(blank=True, null=True)
    platform = models.IntegerField(blank=True, null=True)
    use_type = models.IntegerField(blank=True, null=True)
    main_total = models.IntegerField(blank=True, null=True)
    main_capacity = models.FloatField(blank=True, null=True)
    thermal_imager = models.IntegerField(blank=True, null=True)
    humiture_state = models.IntegerField(blank=True, null=True)
    transformer_structure = models.IntegerField(blank=True, null=True)
    power_period = models.CharField(max_length=255, blank=True, null=True)
    business_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class DayEnergy(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_no = models.CharField(max_length=255, blank=True, null=True)
    newest_value = models.FloatField(blank=True, null=True)
    use_value = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'day_energy'


class Device(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.CharField(max_length=255, blank=True, null=True)
    device_addr = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    auto_tx = models.IntegerField(blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    last_ping = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    port = models.IntegerField(blank=True, null=True)
    dindex = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    platform = models.IntegerField(blank=True, null=True)
    can_break = models.IntegerField(blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    discon_state = models.IntegerField(blank=True, null=True)
    collect_type = models.IntegerField(blank=True, null=True)
    hub_host = models.CharField(max_length=255, blank=True, null=True)
    hub_port = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    parent_id = models.CharField(max_length=255, blank=True, null=True)
    hardware_type = models.IntegerField(blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    gateway_code = models.IntegerField(blank=True, null=True)
    gateway_type = models.CharField(max_length=255, blank=True, null=True)
    gateway_port = models.IntegerField(blank=True, null=True)
    calculate_status = models.IntegerField(blank=True, null=True)
    device_level = models.IntegerField(blank=True, null=True)
    device_parent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'


class DeviceDisconHistory(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_discon_history'


class DeviceGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'device_group'


class DeviceHourEnergy(models.Model):
    company_id = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    day_date = models.DateTimeField(blank=True, null=True)
    h0 = models.FloatField(blank=True, null=True)
    h1 = models.FloatField(blank=True, null=True)
    h2 = models.FloatField(blank=True, null=True)
    h3 = models.FloatField(blank=True, null=True)
    h4 = models.FloatField(blank=True, null=True)
    h5 = models.FloatField(blank=True, null=True)
    h6 = models.FloatField(blank=True, null=True)
    h7 = models.FloatField(blank=True, null=True)
    h8 = models.FloatField(blank=True, null=True)
    h9 = models.FloatField(blank=True, null=True)
    h10 = models.FloatField(blank=True, null=True)
    h11 = models.FloatField(blank=True, null=True)
    h12 = models.FloatField(blank=True, null=True)
    h13 = models.FloatField(blank=True, null=True)
    h14 = models.FloatField(blank=True, null=True)
    h15 = models.FloatField(blank=True, null=True)
    h16 = models.FloatField(blank=True, null=True)
    h17 = models.FloatField(blank=True, null=True)
    h18 = models.FloatField(blank=True, null=True)
    h19 = models.FloatField(blank=True, null=True)
    h20 = models.FloatField(blank=True, null=True)
    h21 = models.FloatField(blank=True, null=True)
    h22 = models.FloatField(blank=True, null=True)
    h23 = models.FloatField(blank=True, null=True)
    h24 = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_hour_energy'


class DeviceManufacturer(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'device_manufacturer'


class DeviceModel(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    manufacturer_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'device_model'


class DeviceParams(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    params_type = models.IntegerField(blank=True, null=True)
    warn_up = models.FloatField(blank=True, null=True)
    warn_down = models.FloatField(blank=True, null=True)
    error_up = models.FloatField(blank=True, null=True)
    error_down = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    channel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_params'


class DeviceProtocol(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'device_protocol'


class DeviceSeries(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'device_series'


class DeviceStatusLog(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    device_no = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_status_log'


class DeviceThreshold(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    threshold_number = models.IntegerField(blank=True, null=True)
    threshold_value = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_threshold'


class DeviceType(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    series_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'device_type'


class Dtu(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    dtu_id = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'dtu'


class EnergyLevel(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    level = models.IntegerField(blank=True, null=True)
    city_id = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'energy_level'


class EnergyMeasurement(models.Model):
    device_no = models.CharField(primary_key=True, max_length=255)
    week_power = models.FloatField(blank=True, null=True)
    lastweek_power = models.FloatField(blank=True, null=True)
    power_range = models.FloatField(blank=True, null=True)
    power_rate = models.FloatField(blank=True, null=True)
    newest_value = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy_measurement'


class EnergyPrice(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    city_id = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'energy_price'


class EnergyReport(models.Model):
    device_no = models.CharField(primary_key=True, max_length=50)
    newest_val = models.FloatField(blank=True, null=True)
    today_val = models.FloatField(blank=True, null=True)
    yesterday_val = models.FloatField(blank=True, null=True)
    currmonth_val = models.FloatField(db_column='currMonth_val', blank=True, null=True)  # Field name made lowercase.
    lastmonth_val = models.FloatField(db_column='lastMonth_val', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy_report'


class ExceptionNotification(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    exception_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exception_notification'


class Exceptions(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    params_type = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    warn_up = models.FloatField(blank=True, null=True)
    warn_down = models.FloatField(blank=True, null=True)
    error_up = models.FloatField(blank=True, null=True)
    error_down = models.FloatField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    disposed = models.IntegerField(blank=True, null=True)
    silent = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    memorandum = models.CharField(max_length=255, blank=True, null=True)
    operation_user = models.CharField(max_length=255, blank=True, null=True)
    inform = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exceptions'


class GatewayDevice(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    gateway_type = models.CharField(max_length=255, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    collect_period = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'gateway_device'


class GatewayType(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'gateway_type'


class IotTelecomSubsrcibe(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    subscribe_id = models.CharField(max_length=255, blank=True, null=True)
    subscribe_url = models.CharField(max_length=255, blank=True, null=True)
    callback_url = models.CharField(max_length=255, blank=True, null=True)
    notify_type = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iot_telecom_subsrcibe'


class LatestData(models.Model):
    device_id = models.CharField(max_length=255)
    type = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    des = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'latest_data'


class Message(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'message'


class MessageRead(models.Model):
    message_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'message_read'


class OnetDevice(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_name = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    device_alias = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    imei = models.CharField(max_length=255, blank=True, null=True)
    imsi = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    onet_id = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    online_state = models.IntegerField(blank=True, null=True)
    device_status = models.IntegerField(blank=True, null=True)
    onet_type = models.IntegerField(blank=True, null=True)
    enable_state = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'onet_device'


class OnetDeviceData(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    od_id = models.CharField(max_length=255, blank=True, null=True)
    temp_value = models.FloatField(blank=True, null=True)
    humi_value = models.FloatField(blank=True, null=True)
    valtage_value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onet_device_data'


class OnetDeviceError(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    od_id = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    data_type = models.IntegerField(blank=True, null=True)
    error_value = models.FloatField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    error_status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    recover_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onet_device_error'


class OnetDeviceParam(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    od_id = models.CharField(max_length=255, blank=True, null=True)
    temp_upper = models.FloatField(blank=True, null=True)
    temp_lower = models.FloatField(blank=True, null=True)
    humidness_upper = models.FloatField(blank=True, null=True)
    humidness_lower = models.FloatField(blank=True, null=True)
    voltage_error = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onet_device_param'


class OnetDeviceType(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'onet_device_type'


class Province(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    sys_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class ReleaseVersion(models.Model):
    android = models.FloatField(blank=True, null=True)
    ios = models.FloatField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'release_version'


class Role(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'role'


class ServiceLog(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_no = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'service_log'


class SetInterval(models.Model):
    hours = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    platform = models.IntegerField(blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_interval'


class SysConfig(models.Model):
    android_version = models.FloatField(blank=True, null=True)
    android_content = models.CharField(max_length=255, blank=True, null=True)
    android_link = models.CharField(max_length=255, blank=True, null=True)
    ios_version = models.FloatField(blank=True, null=True)
    ios_content = models.CharField(max_length=255, blank=True, null=True)
    ios_link = models.CharField(max_length=255, blank=True, null=True)
    wechat_link = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    run_env = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    notice_email = models.CharField(max_length=255, blank=True, null=True)
    notice_phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_config'


class SysNews(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    news_abstract = models.CharField(max_length=255, blank=True, null=True)
    cover = models.CharField(max_length=255, blank=True, null=True)
    xindex = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_news'


class ThermalImager(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_no = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    model_id = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.CharField(max_length=255, blank=True, null=True)
    channel_ip = models.CharField(max_length=255, blank=True, null=True)
    http_port = models.IntegerField(blank=True, null=True)
    rtsp_port = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    protocol_id = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    heat_status = models.IntegerField(blank=True, null=True)
    video_status = models.IntegerField(blank=True, null=True)
    nvr_id = models.CharField(max_length=255, blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    hav_nvr = models.IntegerField(blank=True, null=True)
    hav_ptz = models.IntegerField(blank=True, null=True)
    network_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    video_nvr_stream = models.CharField(max_length=255, blank=True, null=True)
    heat_nvr_stream = models.CharField(max_length=255, blank=True, null=True)
    video_direct_stream = models.CharField(max_length=255, blank=True, null=True)
    heat_direct_stream = models.CharField(max_length=255, blank=True, null=True)
    camera_video_code = models.CharField(max_length=255, blank=True, null=True)
    camera_thermal_code = models.CharField(max_length=255, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thermal_imager'


class ThermalImagerCoordinate(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    thermal_imager_id = models.CharField(max_length=255, blank=True, null=True)
    p_1 = models.CharField(db_column='P_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_2 = models.CharField(db_column='P_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_3 = models.CharField(db_column='P_3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_4 = models.CharField(db_column='P_4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_5 = models.CharField(db_column='P_5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    p_6 = models.CharField(db_column='P_6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a_1 = models.CharField(db_column='A_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a_2 = models.CharField(db_column='A_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a_3 = models.CharField(db_column='A_3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a_4 = models.CharField(db_column='A_4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a_5 = models.CharField(db_column='A_5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    a_6 = models.CharField(db_column='A_6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    line = models.CharField(max_length=255, blank=True, null=True)
    collect_rate = models.IntegerField(blank=True, null=True)
    error_temp = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thermal_imager_coordinate'


class ThermalImagerError(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    thermal_imager_id = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    param = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    error_temp = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    recover_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thermal_imager_error'


class ThermalImagerTemp(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    thermal_imager_id = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    param = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thermal_imager_temp'


class ThresholdParams(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    param_number = models.IntegerField(blank=True, null=True)
    param = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    pindex = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'threshold_params'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    role_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    url = models.CharField(max_length=255, blank=True, null=True)
    job = models.CharField(max_length=255, blank=True, null=True)
    platform = models.IntegerField(blank=True, null=True)
    area_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserCompany(models.Model):
    user_id = models.CharField(max_length=250)
    company_id = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'user_company'


class UserProduct(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_product'


class VideoRecorder(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_no = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    model_id = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.CharField(max_length=255, blank=True, null=True)
    channel_ip = models.CharField(max_length=255, blank=True, null=True)
    channel_port = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    enable = models.IntegerField(blank=True, null=True)
    protocol_id = models.CharField(max_length=255, blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_recorder'


class WasionSyncInfo(models.Model):
    device_date = models.DateTimeField(blank=True, null=True)
    company_date = models.DateTimeField(blank=True, null=True)
    group_date = models.DateTimeField(blank=True, null=True)
    real_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wasion_sync_info'
