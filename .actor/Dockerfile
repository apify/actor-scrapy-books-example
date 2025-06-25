FROM apify/actor-python:3.13

# Install Debian packages.
RUN apt-get update && \
    apt-get install -yq \
        git && \
    rm -rf /var/lib/apt/lists/*

# Install uv package manager.
RUN pip install --upgrade pip && \
    pip install uv

# Copy python config files and install dependencies.
COPY pyproject.toml ./
COPY uv.lock ./
RUN uv export --no-hashes --no-dev | \
    pip install -r /dev/stdin --no-dependencies

# Copy the source code of the Actor.
COPY books_scraper/ ./books_scraper/

# Use compileall to ensure the runnability of the Actor Python code.
RUN python3 -m compileall -q .

# Specify how to launch the source code of your Actor.
CMD ["python3", "-m", "books_scraper"]
