from __future__ import annotations

from typing import TYPE_CHECKING

from scrapy.exceptions import DropItem

from .items import BookItem

if TYPE_CHECKING:
    from scrapy import Spider

# Maps the rating word scraped from the CSS class (e.g. 'star-rating Three') to an int.
RATING_WORDS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
}


class CleaningPipeline:
    """Clean scraped data, dropping any item whose required fields are missing or malformed."""

    # `spider` is required by the Scrapy item-pipeline interface but unused here.
    def process_item(self, item: BookItem, spider: Spider) -> BookItem:  # noqa: ARG002
        """Normalize the raw scraped fields into typed values.

        Raises:
            DropItem: If a required field is missing or cannot be parsed. Dropping the single
                offending item lets the rest of the crawl finish instead of failing the run.
        """
        raw_title = item.get('title') or ''
        raw_price = item.get('price') or ''
        raw_rating = item.get('rating') or ''
        raw_in_stock = item.get('in_stock') or ''

        title = raw_title.strip()
        if not title:
            raise DropItem('Missing book title.')

        try:
            price = float(raw_price.replace('£', '').strip())
        except ValueError as exc:
            raise DropItem(f'Unparsable price {raw_price!r} for {title!r}.') from exc

        # The rating class looks like 'star-rating Three'; the last word is the rating.
        rating_words = raw_rating.split()
        rating = RATING_WORDS.get(rating_words[-1].lower()) if rating_words else None
        if rating is None:
            raise DropItem(f'Unknown rating {raw_rating!r} for {title!r}.')

        return BookItem(
            title=title,
            price=price,
            rating=rating,
            in_stock='in stock' in raw_in_stock.lower(),
        )
