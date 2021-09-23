import scrapy
from scrapy.loader import ItemLoader

from ..items import DefaultItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['https://example.com/']
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "ITEM_PIPELINES": {
            "default.pipelines.DefaultPipeline": 300
        }
    }

    def parse(self, response, **kwargs):
        self.logger.info(f'{response.url}')
        # testing with yielding url
        loader = ItemLoader(DefaultItem())
        loader.add_value('url', response.url)
        yield loader.load_item()
