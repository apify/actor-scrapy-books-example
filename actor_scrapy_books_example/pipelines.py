from __future__ import annotations

from typing import TYPE_CHECKING

from .items import BookItem

if TYPE_CHECKING:
    from scrapy import Spider


class CleaningPipeline:
    """Clean scraped data."""

    # `spider` is required by the Scrapy item-pipeline interface but unused here.
    def process_item(self, item: BookItem, spider: Spider) -> BookItem:  # noqa: ARG002
        """Normalize the raw scraped fields into typed values."""
        number_map = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
        }
        return BookItem(
            title=item['title'],
            price=float(item['price'].replace('£', '')),
            rating=number_map[item['rating'].split(' ')[1].lower()],
            in_stock=bool(item['in_stock'].lower() == 'in stock'),
        )
