from __future__ import annotations

from typing import TYPE_CHECKING, Generator

from scrapy import Request, Spider

from ..items import BookItem

if TYPE_CHECKING:
    from scrapy.responsetypes import Response


class BookSpider(Spider):
    """Scrape books from https://books.toscrape.com/."""

    name = "book_spider"
    start_urls = ["https://books.toscrape.com/"]
    allowed_domains = ["books.toscrape.com"]

    def parse(self, response: Response) -> Generator[BookItem | Request, None, None]:
        self.logger.info("BookSpider is parsing %s...", response)
        articles = response.css("article.product_pod")

        for article in articles:
            yield BookItem(
                title=article.css("h3 > a::attr(title)").get().strip(),
                price=article.css(".price_color::text").get().strip(),
                rating=article.css(".star-rating::attr(class)").get().strip(),
                in_stock=article.css(".instock.availability::text").getall()[1].strip(),
            )

        next_page_link = response.css("li.next a::attr(href)").extract_first()
        if next_page_link:
            yield response.follow(next_page_link)
