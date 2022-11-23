from scrapy import Request, Spider
import custom_settings_config

class BrowserHtmlSpider(Spider):
    name = 'browser_html'

    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        pass # your code here

    def parse(self, response):
        pass # your code here