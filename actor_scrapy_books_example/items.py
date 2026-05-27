from __future__ import annotations

import scrapy


class BookItem(scrapy.Item):
    """A scraped book: title, rating, price, and stock status."""

    title = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    in_stock = scrapy.Field()
