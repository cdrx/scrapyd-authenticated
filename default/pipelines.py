# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import asyncio


class DefaultPipeline:
    async def process_item(self, item, spider):
        spider.logger.info("Running Asyncio Pipeline: Testing Sleep for 2 seconds")
        # testing with running asycio sleep
        await self.test_sleep(2, spider)
        spider.logger.info(f"Ending sleep with item: {item}")
        return item

    async def test_sleep(self, seconds, spider):
        await asyncio.sleep(seconds)
        spider.logger.info('hello from test_sleep')