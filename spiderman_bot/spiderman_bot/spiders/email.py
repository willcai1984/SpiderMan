# -*- coding: utf-8 -*-
import scrapy
from ..util import EmailSend
from bank.models import Tender
from bank.models import Mail


class EmailtestSpider(scrapy.Spider):
    name = 'email'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    # # 在爬虫启动和关闭的时候，分别发送邮箱，通知爬虫管理者。
    # def start_requests(self):
    #     email = EmailSend()
    #     content = '爬虫启动时间：{}'.format(datetime.now())
    #     email.send_text_email('xxxxxxxxx@qq.com', 'yyyyyyyy@qq.com', '爬虫启动', content)
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass

    def closed(self, reason):
        # 爬虫关闭的时候，会调用这个方法
        content_tuple_list = []
        tenders_not_notice = Tender.objects.filter(is_delete=0).filter(is_notice=0)
        title = ''
        for tender in tenders_not_notice:
            title = tender.title
            content_tuple_list.append((tender.location, tender.source_site, tender.title, tender.pub_date, tender.url))
        receivers = []
        for mail in Mail.objects.filter(is_delete=0):
            receivers.append(mail.receive_mail)
        e = EmailSend()
        subject = "更新%s等%s条招标信息" % (title, len(content_tuple_list))
        r = e.email_send(receivers, subject, content_tuple_list)
        if r:
            tenders_not_notice.update(is_notice=1)