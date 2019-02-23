# -*- coding: utf-8 -*-
'spider_main'
from new1_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownload()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def craw(self,root_url):
        pass

if __name__=="__main__":
    root_url="https://baike.baidu.com/item/%E8%BF%A6%E5%8B%92%E5%BA%95/20231074"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)