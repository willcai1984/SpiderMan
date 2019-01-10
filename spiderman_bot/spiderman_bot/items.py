# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# from .util import DjangoItemPlus
from scrapy_djangoitem import DjangoItem
from bank.models import Tender


class TenderItem(DjangoItem):
    django_model = Tender
