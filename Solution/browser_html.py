from scrapy import Request, Spider
import custom_settings_config

class BrowserHtmlSpider(Spider):
    name = 'browser_html'

    custom_settings = custom_settings_config.custom_settings

    def start_requests(self):
        yield Request(
            "http://quotes.toscrape.com",
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                },
            },
        )

    def parse(self, response):
        browser_html: str = response.text # browser html
        for quote in response.css('.quote'):            
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tags a.tag::text').getall(),
            }