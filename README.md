# Actor Scrapy Books Example

This project serves as an example of Python Scrapy project. It scrapes book data from [books.toscrape.com](https://books.toscrape.com/).

## Getting Started

### Install Apify CLI

To use this scraper, you need to install the Apify CLI. Follow the instructions [here](https://docs.apify.com/cli/docs/installation).

### Install Python and Virtualenv

Make sure you have Python installed. If not, download it [here](https://www.python.org/). Any version supported by [Apify SDK](https://pypi.org/project/apify/) and [Scrapy](https://pypi.org/project/Scrapy/) should be fine.

Additionally, install [uv](https://docs.astral.sh/uv/) package manager.

```bash
pip install uv
```

## Run the Actor locally

### Prepare Python environment

Install Python dependencies:

```bash
make install-dev
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### Run the scraper as Scrapy project

The project is still runnable as a Scrapy project. Execute the following command:

```bash
scrapy crawl book_spider -o books.json
```

### Run the scraper as Apify Actor

Run the scraper as an Apify Actor using:

```bash
apify run --purge
```

## Deploy on Apify

### Log in to Apify

You will need to provide your [Apify API Token](https://console.apify.com/account/integrations) to complete this action.

```bash
apify login
```

### Deploy your Actor

This command will deploy and build the Actor on the Apify Platform. You can find your newly created Actor under [Actors -> My Actors](https://console.apify.com/actors?tab=my).

```Bash
apify push
```

## Documentation reference

To learn more about Apify and Actors, take a look at the following resources:

- [Integrating Scrapy projects](https://docs.apify.com/cli/docs/integrating-scrapy)
- [Apify SDK for Python](https://docs.apify.com/sdk/js)
- [Apify Platform](https://docs.apify.com/platform)
- [Join our developer community on Discord](https://discord.com/invite/jyEM2PRvMU)
