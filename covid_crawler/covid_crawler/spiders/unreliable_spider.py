import scrapy


class UnreliableSpiderSpider(scrapy.Spider):
    name = "unreliable_spider"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
