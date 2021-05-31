import scrapy
from ..items import StackItem

class StackSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]

    def start_requests(self):
        urls = [
            "http://stackoverflow.com/questions?pagesize=50&sort=newest",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        questions = scrapy.Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item