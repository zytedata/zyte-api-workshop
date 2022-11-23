from scrapy import Request, Spider
from base64 import b64decode, decodebytes
import custom_settings_config

class BrowserActionGenericSpider(Spider):
    name = 'browser_action_generic'

    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        yield Request(
            "https://quotes.toscrape.com/scroll",
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                    "screenshot": True,
                    "screenshotOptions": {
                        "fullPage": True
                        },
                    "actions": [{
                            "action": "scrollBottom",
                        }
                    ]
                }
            }
        )
        
    def parse(self, response):
        quote_count = len(response.css(".quote"))
        self.logger.info("Quote Count: ", quote_count)

        screenshot: bytes = b64decode(response.raw_api_response["screenshot"]) # decode base64 response
        with open("output_quote.jpg", "wb") as fh: 
            fh.write(screenshot) # write bytes to the output.jpg file

