
custom_settings = dict(
        DOWNLOAD_HANDLERS = {
            "http": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
            "https": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
        },
        TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        ZYTE_API_KEY = "YOUR ZYTE API KEY HERE",
        ZYTE_API_TRANSPARENT_MODE= True,

)