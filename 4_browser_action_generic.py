from scrapy import Request, Spider
from base64 import b64decode, decodebytes
import custom_settings_config


class BrowserActionGenericSpider(Spider):
    name = 'browser_action_generic'

    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        pass # your code here
        
    def parse(self, response):
        pass # your code here
