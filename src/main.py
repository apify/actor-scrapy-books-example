from __future__ import annotations

from scrapy.crawler import CrawlerRunner
from scrapy.utils.defer import deferred_to_future

from apify import Actor
from apify.scrapy import apply_apify_settings

# Import your Scrapy spider here
from .spiders.book import BookSpider as Spider


async def main() -> None:
    """Apify Actor main coroutine for executing the Scrapy spider."""
    async with Actor:
        Actor.log.info("Actor is being executed...")

        # Process Actor input.
        actor_input = await Actor.get_input() or {}
        proxy_config = actor_input.get("proxyConfiguration")

        # Get Scrapy project settings with custom configurations.
        settings = apply_apify_settings(proxy_config=proxy_config)

        # Create CrawlerRunner and execute the Scrapy spider.
        crawler_runner = CrawlerRunner(settings)
        crawl_deferred = crawler_runner.crawl(Spider)
        await deferred_to_future(crawl_deferred)
