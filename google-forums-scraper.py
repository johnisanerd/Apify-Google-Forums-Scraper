"""
Google Forums API: A Quick Start Example
See more at: https://apify.com/johnvc/google-forums-search-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-forums-search-api/input-schema?fpr=9n7kx3

This script shows how to call the Google Forums API on Apify from Python and read
its structured JSON output. It exercises several input parameters so you can see
what is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# max_pages is kept at 1 to keep this first run inexpensive (each page is billed
# separately). Raise it once you have your own API key and know your budget.
run_input = {
    "q": "best coffee brewing methods",
    "location": "Austin, TX, Texas, United States",
    "gl": "us",                      # country code
    "hl": "en",                      # language code
    "max_pages": 1,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-forums-search-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset (one item per page)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} page(s) of results.\n")

# Show a few forum results from each page.
for item in items:
    meta = item.get("search_metadata", {})
    print(f"Total results: {meta.get('total_results')}")
    for result in (item.get("forum_results") or [])[:5]:
        print(f"  {result.get('position')}. {result.get('title')}  [{result.get('source')}]")
        print(f"     {result.get('link')}")
    print()
