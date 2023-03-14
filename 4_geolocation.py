from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
import json, scrapy, custom_settings_config, os
from base64 import b64decode, decodebytes
import datetime

class AmazonbooksSpider(scrapy.Spider):
    name = 'amazonbooks'
    allowed_domains = ['amazon.co.uk']
    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        yield scrapy.Request(
            "https://www.amazon.co.uk/gp/bestsellers/books",
            meta = {
                "zyte_api": {
                    "screenshot": True,
                    "geolocation": "AU",
                }
            }
        )

    def parse(self, response):
        screenshot: bytes = b64decode(response.raw_api_response["screenshot"])  # decode base64 response
        with open("../amazon_in/output_4.jpg", "wb") as fh:
            fh.write(screenshot)  # write bytes to the output.jpg file