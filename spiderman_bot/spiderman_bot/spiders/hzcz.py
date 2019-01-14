# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from ..items import TenderItem


class HzczSpider(scrapy.Spider):
    name = 'hzcz'
    allowed_domains = ['hzft.gov.cn']
    start_urls = ['http://www.hzft.gov.cn/col/col146/index.html']

    def parse(self, response):
        # 返回报文不规范，用bs4的find处理，不用css和xpath等精确报文匹配模式
        # tender_trs = response.css("div.default_pgContainer>table>tbody>tr")
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("div", id="1079")
        for entry in re.findall(r"<tr>.*</tr>", result.text):
            item = TenderItem()
            s = BeautifulSoup(entry, "html.parser")
            item['title'] = s.find("a")["title"]
            # item['notice_id'] = tender_tr.css("td>div>a.bt_link::href").extract()
            item['notice_id'] = s.find("a")["href"]
            item['url'] = "http://www.hzft.gov.cn" + s.find("a")["href"]
            item['pub_date'] = re.sub("\[|\]", "", s.find_all("td")[-1].string)
            item['location'] = "杭州"
            item['source_site'] = '杭州财政'
            yield item
