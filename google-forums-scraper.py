"""
Google Forums Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/google-forums-search-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-forums-search-api/input-schema?fpr=9n7kx3

This script demonstrates how to scrape forum threads and discussions from the
Google Forums search tab using the Google Forums API scraper on Apify.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "q": "python web scraping tutorial",
    "location": "United States",
    "gl": "us",
    "hl": "en",
    "safe": "off",
    "max_pages": 2,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-forums-search-api").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
