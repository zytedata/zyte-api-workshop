import json
from scrapy import Request, Spider
import custom_settings_config
import logging

class GeolocationSpider(Spider):
    name = 'geolocation'
    
    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        pass # your code here
    
    def parse(self, response):
        pass # your code here