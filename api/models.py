# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now, localtime


# CharField 可变长度字符串
class Business(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True,
                                    null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'business'


class ChannelSettings(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    channel_index = models.IntegerField(blank=True, null=True)
    channel_type = models.IntegerField(blank=True, null=True)
    channel_alias = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'city'


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)  # 小于254字符
    content = models.TextField()  # 大于254字符使用该field
    removed = models.BooleanField(default=False)  # 是否被删除
    created_time = models.DateTimeField(default=now())
    removed1 = models.NullBooleanField(default=False, null=False)

    # 引用其他表,on_delete 目前指定设置为空,并且null=True
    email = models.ForeignKey('EmailOffer', on_delete=models.SET_NULL, null=True)

    # max_length 最大长度

    class Meta:
        managed = True
        db_table = "article"


class EmailOffer(models.Model):
    name = models.EmailField(max_length=255)
    id = models.UUIDField(primary_key=True)
    own_company = models.CharField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = 'email_offer'


class CollectorManagerSettings(models.Model):
    ping = models.DateTimeField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        ordering = ["ping"]
        db_table = 'collector_manager_settings'


# 表关系,外键和表关系
# 两个表通过外键关联
# 外键的删除操作,使用SET(User.objects.get(id=4))或者SET_NULL(但是当前项nul,必须设置为Null=True)
# 一对多的关联操作 设置一个文章多个分类
# 多对一的操作  获取一个分类多个文章,一对多的对应访问
# 一对一: 一对一是通过models.OneToOneField()来实现的,一对一的对应访问,一对一的关系应该是,级联删除的
# 多对多关系,文章和标签的关系,一个标签可以被多个标签使用,一个文章有多个标签
# orm查询操作

# 查询条件的使用
# 包含,模糊查询
#  id 等于14的邮箱
email = EmailOffer.objects.get(id__exact=14)
email = EmailOffer.objects.filter(id=14)
email1 = EmailOffer.objects.get(name__iexact=None)

# 使用聚合函数
