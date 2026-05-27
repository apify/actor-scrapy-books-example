# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

An example Scrapy project wrapped as an Apify Actor. It scrapes book data
(title, price, rating, stock) from [books.toscrape.com](https://books.toscrape.com/)
and stores items in the run's default dataset.

## How it runs (important)

The Actor entrypoint is **`python -m actor_scrapy_books_example`**, *not*
`scrapy crawl`. The order in `__main__.py` matters:

1. `install_reactor('...AsyncioSelectorReactor')` — must happen before any other
   Twisted/Scrapy import.
2. set `SCRAPY_SETTINGS_MODULE = 'actor_scrapy_books_example.settings'`.
3. `run_scrapy_actor(main())` (from `apify.scrapy`).

`main.py` reads input, builds settings via `apply_apify_settings(proxy_config=...)`,
and runs `BookSpider` through a `CrawlerRunner`. Because the settings module is
set in code, `scrapy.cfg` is only needed to run as a *plain* Scrapy project
(`scrapy crawl book_spider`) — it is not used by the Actor and is not copied
into the image.

## Layout

- `actor_scrapy_books_example/`
  - `__main__.py` — reactor install + Actor bootstrap (see above).
  - `main.py` — Apify Actor coroutine; wires proxy + runs the spider.
  - `spiders/book.py` — `BookSpider`: parses listing pages, yields a `BookItem`
    per product, follows pagination. `DEPTH_LIMIT = 50` (50 listing pages).
  - `items.py` — `BookItem` (title, rating, price, in_stock).
  - `pipelines.py` — `CleaningPipeline`: normalizes price→float, rating→int,
    in_stock→bool.
  - `settings.py` — Scrapy settings (asyncio reactor, robots obey, pipelines).
- `.actor/` — Apify manifest, `input_schema.json`, `output_schema.json`,
  `dataset_schema.json`, `Dockerfile`.

## Commands

uv-managed project (`pyproject.toml` + `uv.lock`, `package = false`).

```bash
uv sync                      # install deps into .venv/
uv run poe check-code        # lint + type-check — run before committing
uv run poe lint              # ruff format --check && ruff check
uv run poe type-check        # ty check
uv run poe format            # ruff check --fix && ruff format

apify run --purge            # run as an Actor locally (uses the local .venv, not Docker)
apify run -i '{}'            # pass {} to skip Apify Proxy when not logged in
```

The README's `make install-dev` / `scrapy crawl` instructions are stale: the
Makefile was replaced by poe, and the Actor runs via `python -m ...`.

## Conventions / gotchas

- Scrapy class attrs (`start_urls`, `allowed_domains`) keep `# noqa: RUF012`;
  `__main__.py`'s late imports keep `# noqa: E402` (reactor must install first).
- ruff: line length 120, single quotes, `select = ["ALL"]` with the ignores in
  `pyproject.toml`; types via ty. Keep `uv run poe check-code` green.
- Python 3.14 across `.python-version`, ty, CI, and the Docker base.
- The Dockerfile uses the uv-in-Docker BuildKit pattern (uv binary from
  `ghcr.io/astral-sh/uv:0.11`, `uv sync --locked --no-dev`); build with BuildKit.
- Commit `uv.lock` whenever dependencies change.
