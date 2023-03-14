from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader
import json, scrapy, custom_settings_config, os


class AmazonbooksSpider(scrapy.Spider):
    name = 'amazonbooks'
    allowed_domains = ['amazon.co.uk']
    start_urls = ['https://www.amazon.co.uk/gp/bestsellers/books']

    custom_settings = custom_settings_config.custom_settings

    def parse(self, response):
        raw_data = response.css('[data-client-recs-list]::attr(data-client-recs-list)').get()
        data = json.loads(raw_data)
        for item in data:
            url = 'https://www.amazon.co.uk/dp/{}'.format(item['id'])
            yield scrapy.Request(url, callback=self.parse_item,
                                 meta={'rank': item['metadataMap']['render.zg.rank'], 'id': item['id']})

        next_page = response.css('.a-last a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_item(self, response):
        rank = response.meta.get('rank')
        id = response.meta.get('id')
        authors = response.css(
            '#bylineInfo_feature_div #bylineInfo span.author.notFaded a.a-link-normal::text').getall()[2:]

        yield {
            "book_url": response.url,
            'author': authors,
            'rank': rank,
            'id': id,
            'book_title': response.css('#productTitle::text').get(),
            'price': response.css('.a-color-price::text').get(),
            'cover': response.css('#main-image::attr(src)').get()
        }
