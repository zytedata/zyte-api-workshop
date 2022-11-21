from scrapy import Request, Spider
from base64 import b64decode, decodebytes


class ScreenshotPySpider(Spider):
    name = 'screenshot'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def start_requests(self):
        yield Request(
            "https://quotes.toscrape.com",
            meta = {
                "zyte_api_automap": {
                    "screenshot": True,
                }
            }
        )
    
    def parse(self, response):
        screenshot: bytes = b64decode(response.raw_api_response["screenshot"]) # decode base64 response
        with open("output.jpg", "wb") as fh: 
            fh.write(screenshot) # write bytes to the output.jpg file