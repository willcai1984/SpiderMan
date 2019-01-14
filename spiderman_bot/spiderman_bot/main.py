# -*- coding: utf-8 -*-
# Author:Will
"""
增加main函数，方便本地调试
"""
import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "hzcz"])  # 这句代码会执行爬虫类中 name = "myspider_haha"的类
# execute(["scrapy", "crawl", "zjzfcg"])
execute(["scrapy", "crawl", "email"])
