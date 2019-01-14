# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from ..items import TenderItem
import urllib.parse
import json
import time


class ZJZFCGSpider(scrapy.Spider):
    name = 'zjzfcg'
    allowed_domains = ['zjzfcg.gov.cn']
    start_urls = ['http://www.hzft.gov.cn/col/col146/index.html']

    # 在爬虫启动和关闭的时候，分别发送邮箱，通知爬虫管理者。
    def start_requests(self):
        start_urls = [self._process_url('存款'), self._process_url('存放')]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def _process_url(self, key):
        url = "http://manager.zjzfcg.gov.cn/cms/api/cors/getRemoteResults?"
        values = (('pageSize', '15'),
                  ('pageNo', '1'),
                  ('noticeType', '0'),
                  ('url', 'http://notice.zcy.gov.cn/new/noticeSearch'),
                  ('keyword', key)
                  )
        return url + urllib.parse.urlencode(values)

    def parse(self, response):
        tender_dict = json.loads(response.text)
        articles = tender_dict.get("articles")
        for article in articles:
            item = TenderItem()
            item["notice_id"] = article.get("id")
            item["bid_menu"] = article.get("mainBidMenuName")
            item["title"] = article.get("title")
            item["project_code"] = article.get("projectCode")
            item["pub_date"] = time.strftime("%Y-%m-%d", time.localtime(float(article.get("pubDate")[:10])))
            item["location"] = article.get("districtName")
            item["url"] = article.get("url")
            item["source_site"] = "浙江采购"
            yield item
