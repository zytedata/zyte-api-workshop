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
            "https://www.amazon.co.uk/dp/178685807X",
            meta = {
                "zyte_api": {
                    "screenshot": True,
                    "browserHtml": True,
                    "actions": [
                        {
                            "action": "click",
                            "selector": {
                                "type": "css",
                                "value": ".cip-a-size-small"
                            },
                            "delay": 0,
                            "button": "left",
                            "onError": "return"
                        },
                        {
                            "action": "type",
                            "selector": {
                                "type": "css",
                                "value": "#GLUXZipUpdateInput"
                            },
                            "delay": 0,
                            "onError": "return",
                            "text": "NW1 5LJ",  # BT23 4AA
                        },
                        {
                            "action": "click",
                            "selector": {
                                "type": "css",
                                "value": ".a-button-input"
                            },
                            "delay": 0,
                            "button": "left",
                            "onError": "return"
                        }
                    ],
                }
            }
        )

    def parse(self, response):
        screenshot: bytes = b64decode(response.raw_api_response["screenshot"])  # decode base64 response
        with open("../amazon_in/output_5.jpg", "wb") as fh:
            fh.write(screenshot)  # write bytes to the output.jpg file

        yield{
            "book_url": response.url,
            'author': response.css('#bylineInfo a.a-link-normal::text').getall()[2:],
            'book_title': response.css('#productTitle::text').get(),
            'price': response.css('.a-color-price::text').get(),
            'cover': response.css('#main-image::attr(src)').get(),
            'delivery': response.css(
                '#mir-layout-DELIVERY_BLOCK #mir-layout-DELIVERY_BLOCK-slot-SECONDARY_DELIVERY_MESSAGE_LARGE .a-text-bold::text').get(),
        }