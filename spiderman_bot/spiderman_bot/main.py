# -*- coding: utf-8 -*-
# Author:Will
"""
增加main函数，方便本地调试
"""
import sys
import os

# from scrapy.cmdline import execute
# 要增加上一级的路径，获取scrapy.cfg才能使用scrapy cmdline
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute方法中的最后一句代码是sys.exit(cmd.exitcode)，所以当程序执行完一个execute语句后便停止了。
# https://stackoverflow.com/questions/24875280/scrapy-cmdline-execute-stops-script
# execute(["scrapy", "crawl", "hzcz"])  # 这句代码会执行爬虫类中 name = "myspider_haha"的类
# execute(["scrapy", "crawl", "zjzfcg"])
# execute(["scrapy", "crawl", "email"])

os.system('scrapy crawl hzcz')
os.system('scrapy crawl zjzfcg')
os.system('scrapy crawl email')
