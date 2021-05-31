import scrapy
from ..items import TuoitreItem

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class TuoitreThethaoCrawlerSpider(CrawlSpider):
    name = 'tuoitre_thethao_crawler'
    allowed_domains = ['thethao.tuoitre.vn']
    start_urls = ['https://thethao.tuoitre.vn/']

    rules = [
        Rule(LinkExtractor(),
         callback='parse_item', follow=True),
    ]

    def parse_item(self, response):
        s = ""
        title = scrapy.Selector(response).xpath('//*[@id="main-detail"]/div[1]/h1/text()')
        if len(title.extract()) > 0:
            s += str(title.extract()[0]).strip() + ' '

        body = scrapy.Selector(response).xpath('//*[@id="mainContentDetail"]/div')
        body = body.xpath('div[@class="main-content-body"]')

        overview = body.xpath('h2[@class="sapo"]/text()')
        if len(overview.extract()) > 0:
            s += str(overview.extract()[0]).strip() + ' '

        body_elems = body.xpath('div/p/span/text()')
        for elem in body_elems:
            # print(elem.get())
            if len(elem.get()) > 0:
                s += str(elem.get()).strip() + ' '
        
        # print(s)
        s = s.strip()
        if len(s) > 0:
            item = TuoitreItem()
            item['content'] = s
            item['category'] = 'Thể thao'
            yield item
    
class TuoitreCongngheCrawlerSpider(CrawlSpider):
    name = 'tuoitre_congnghe_crawler'
    allowed_domains = ['congnghe.tuoitre.vn']
    start_urls = ['https://congnghe.tuoitre.vn/']

    rules = [
        Rule(LinkExtractor(),
         callback='parse_item', follow=True),
    ]

    def parse_item(self, response):
        s = ""
        title = scrapy.Selector(response).xpath('//*[@id="main-detail"]/div[1]/h1/text()')
        if len(title.extract()) > 0:
            s += str(title.extract()[0]).strip() + ' '

        body = scrapy.Selector(response).xpath('//*[@id="mainContentDetail"]/div')
        body = body.xpath('div[@class="main-content-body"]')

        overview = body.xpath('h2[@class="sapo"]/text()')
        if len(overview.extract()) > 0:
            s += str(overview.extract()[0]).strip() + ' '

        body_elems = body.xpath('div/p/span/text()')
        for elem in body_elems:
            # print(elem.get())
            if len(elem.get()) > 0:
                s += str(elem.get()).strip() + ' '
        
        # print(s)
        s = s.strip()
        if len(s) > 0:
            item = TuoitreItem()
            item['content'] = s
            item['category'] = 'Công nghệ'
            yield item

class TuoitreDulichCrawlerSpider(CrawlSpider):
    name = 'tuoitre_dulich_crawler'
    allowed_domains = ['dulich.tuoitre.vn']
    start_urls = ['https://dulich.tuoitre.vn/']

    rules = [
        Rule(LinkExtractor(),
         callback='parse_item', follow=True),
    ]

    def parse_item(self, response):
        s = ""
        title = scrapy.Selector(response).xpath('//*[@id="main-detail"]/div[1]/h1/text()')
        if len(title.extract()) > 0:
            s += str(title.extract()[0]).strip() + ' '

        body = scrapy.Selector(response).xpath('//*[@id="mainContentDetail"]/div')
        body = body.xpath('div[@class="main-content-body"]')

        overview = body.xpath('h2[@class="sapo"]/text()')
        if len(overview.extract()) > 0:
            s += str(overview.extract()[0]).strip() + ' '

        body_elems = body.xpath('div/p/span/text()')
        for elem in body_elems:
            # print(elem.get())
            if len(elem.get()) > 0:
                s += str(elem.get()).strip() + ' '
        
        # print(s)
        s = s.strip()
        if len(s) > 0:
            item = TuoitreItem()
            item['content'] = s
            item['category'] = 'Du lịch'
            yield item