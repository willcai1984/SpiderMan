from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Mail(models.Model):
    name = models.CharField('用户昵称，可修改', max_length=128, default='')
    receive_mail = models.CharField('接收通知邮箱地址', max_length=128, default='')
    create_time = models.DateTimeField('创建日期', default=timezone.now)
    is_delete = models.IntegerField('逻辑删除，默认0，0正常，1删除', default=0)


class Tender(models.Model):
    title = models.CharField('招标标题', max_length=128, default='')
    create_time = models.DateTimeField('创建日期', default=timezone.now)
    notice_id = models.CharField('唯一ID', max_length=128, default='')
    bid_menu = models.CharField('分类', max_length=32, default='')
    project_code = models.CharField('项目代号', max_length=64, default='')
    pub_date = models.CharField('公布日期', max_length=64, default='')
    end_date = models.CharField('截止日期', max_length=64, default='')
    location = models.CharField('所属区域', max_length=64, default='')
    source_site = models.CharField('来源网站', max_length=32, default='')
    url = models.CharField('跳转链接', max_length=128, default='')
    is_notice = models.IntegerField('是否已通知，默认0，0未通知，1已通知', default=0)
    is_delete = models.IntegerField('逻辑删除，默认0，0正常，1删除', default=0)
