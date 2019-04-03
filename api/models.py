# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now,localtime

# CharField 可变长度字符串
class Business(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        db_table = 'business'


class ChannelSettings(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    channel_index = models.IntegerField(blank=True, null=True)
    channel_type = models.IntegerField(blank=True, null=True)
    channel_alias = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'channel_settings'


class City(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    province_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.
    sys_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'city'


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)  # 小于254字符
    content = models.TextField()  # 大于254字符使用该field
    removed = models.BooleanField(default=False)  # 是否被删除
    created_time = models.DateTimeField(default=now())
    removed1 = models.NullBooleanField(default=False, null=False)

    class Meta:
        db_table = "article"
