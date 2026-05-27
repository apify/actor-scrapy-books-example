from __future__ import annotations

from typing import TYPE_CHECKING

from scrapy import Spider

from actor_scrapy_books_example.items import BookItem

if TYPE_CHECKING:
    from collections.abc import Generator

    from scrapy import Request
    from scrapy.http import Response


class BookSpider(Spider):
    """Scrape books from https://books.toscrape.com/."""

    name = 'book_spider'
    # Scrapy treats these as class-level configuration, so RUF012 (ClassVar) does not apply;
    # annotating them as ClassVar also conflicts with Spider's base attribute types.
    start_urls = ['https://books.toscrape.com/']  # noqa: RUF012
    allowed_domains = ['books.toscrape.com']  # noqa: RUF012

    def parse(self, response: Response) -> Generator[BookItem | Request]:
        """Parse a listing page, yielding a book item per product and following pagination."""
        self.logger.info('BookSpider is parsing %s...', response)
        articles = response.css('article.product_pod')

        for article in articles:
            yield BookItem(
                title=(article.css('h3 > a::attr(title)').get() or '').strip(),
                price=(article.css('.price_color::text').get() or '').strip(),
                rating=(article.css('.star-rating::attr(class)').get() or '').strip(),
                # `::text` returns several nodes split by the inner <i> icon; join them so we
                # capture the availability text regardless of how the markup is whitespaced.
                in_stock=' '.join(article.css('.instock.availability::text').getall()).strip(),
            )

        next_page_link = response.css('li.next a::attr(href)').get()
        if next_page_link:
            yield response.follow(next_page_link)
