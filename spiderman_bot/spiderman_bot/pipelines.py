# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from bank.models import Tender


class SpidermanBotPipeline(object):
    def __init__(self, *args, **kwargs):
        super(SpidermanBotPipeline, self).__init__(*args, **kwargs)
        # notice_id+source_site形成唯一主键
        self.id_set = set()
        for tender_tuple in Tender.objects.filter(is_delete=0).values_list('notice_id', 'source_site'):
            self.id_set.add(''.join(tender_tuple))

    def process_item(self, item, spider):
        notice_id = item['notice_id']
        source_site = item['source_site']
        if notice_id + source_site in self.id_set:
            raise DropItem("Duplicate tender found:%s" % (notice_id + source_site))
        self.id_set.add(notice_id + source_site)
        item.save()
        return item
