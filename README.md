# Scrapy Books Example

An example [Scrapy](https://scrapy.org/) project wrapped as an Apify Actor. It scrapes book data (title, price, rating, availability) from [books.toscrape.com](https://books.toscrape.com/) and stores each book in the run's default dataset.

It shows how to run an existing Scrapy spider on the Apify platform — see [Integrating Scrapy projects](https://docs.apify.com/cli/docs/integrating-scrapy).

## Run locally

This is a [uv](https://docs.astral.sh/uv/)-managed project. You'll also need the [Apify CLI](https://docs.apify.com/cli/docs/installation).

```bash
uv sync                # install dependencies into .venv/
apify run --purge      # run as an Apify Actor (reads local INPUT.json)
```

It also still runs as a plain Scrapy project:

```bash
uv run scrapy crawl book_spider -o books.json
```

## Deploy to Apify

```bash
apify login            # once, with your API token
apify push             # build and deploy the Actor
```

Find your deployed Actor under [Actors → My Actors](https://console.apify.com/actors?tab=my).

## Learn more

- [Integrating Scrapy projects](https://docs.apify.com/cli/docs/integrating-scrapy)
- [Apify SDK for Python](https://docs.apify.com/sdk/python)
- [Apify platform docs](https://docs.apify.com/platform)
