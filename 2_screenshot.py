from scrapy import Request, Spider
from base64 import b64decode, decodebytes


class ScreenshotPySpider(Spider):
    name = 'screenshot'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def start_requests(self):
        pass # your code here

    def parse(self, response):
        pass # your code here
