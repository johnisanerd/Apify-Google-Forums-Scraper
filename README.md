# 🗣️ Google Forums API: Forum Threads and Discussions in Clean JSON

> The most efficient, reliable, and developer-friendly way to use the Google Forums API.

**Actor page:** [apify.com/johnvc/google-forums-search-api](https://apify.com/johnvc/google-forums-search-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/google-forums-search-api/input-schema](https://apify.com/johnvc/google-forums-search-api/input-schema?fpr=9n7kx3)

The Google Forums API runs a search on Google's dedicated Forums tab and returns clean, structured JSON. One call surfaces ranked threads from Reddit, Quora, Stack Overflow, Facebook groups, and thousands of community platforms at once, with title, link, snippet, source, displayed metadata (comments and recency), and position. It supports 40+ countries, country and language localization, device emulation, safe-search and duplicate filters, and pagination.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Forums-Scraper.git
   cd Apify-Google-Forums-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-forums-scraper.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-forums-scraper.py
```

## Why Use This Google Forums API?

**One query, every platform.** Google's Forums tab aggregates Reddit, Quora, Stack Overflow, Facebook groups, and niche communities. Submit one query and get ranked forum results from across the public web, instead of maintaining a separate integration per platform.

**Precision geo-targeting.** Filter by country code (`gl`), interface language (`hl`), result-language restriction (`lr`), and a location string for fine-grained localization.

**Scalable pagination.** Set `max_pages` for a shallow sample or a deep dataset. Each page is pushed as its own dataset item for easy streaming and filtering.

**Predictable, pay-per-use pricing.** Per run plus per page processed, with no subscription. You pay only for what you fetch.

**Built for AI and research.** Forum content is among the richest sources of authentic opinion and domain expertise. Collect it at scale for sentiment analysis, brand monitoring, competitive intelligence, and LLM training data, or load it as an MCP tool for Claude and Cursor.

## Features

### Core Capabilities
- **Forums-tab search** across Reddit, Quora, Stack Overflow, and community platforms
- **Localization** by country, interface language, and result language
- **Device emulation** (desktop, mobile, tablet)
- **Safe-search, auto-correct, and duplicate filters**
- **Multi-page pagination** with a configurable page cap

### Data Quality
- **Consistent JSON** with the same field structure across every source
- **Per-result detail**: position, title, link, snippet, source, and displayed metadata
- **Source attribution** including subreddit or community name
- **Per-page dataset items** for accurate billing and easy downstream filtering

## Usage Examples

### Basic search
```json
{
  "q": "best coffee brewing methods",
  "max_pages": 1
}
```

### Localized, multi-page search
```json
{
  "q": "python vs java",
  "location": "United States",
  "gl": "us",
  "hl": "en",
  "safe": "off",
  "max_pages": 3
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `q` | `string` | Yes | - | Search query for forum discussions. |
| `location` | `string` | No | (none) | Location string for localized results, e.g. `Austin, TX, Texas, United States`. |
| `device` | `string` | No | `desktop` | Device to emulate: `desktop`, `mobile`, or `tablet`. |
| `gl` | `string` | No | (none) | Country code (ISO 3166-1 alpha-2, lowercase). 40+ markets. |
| `hl` | `string` | No | (none) | Interface language code (ISO 639-1). |
| `lr` | `string` | No | (none) | Result-language restriction, e.g. `lang_en`. |
| `safe` | `string` | No | `off` | Safe search: `active` or `off`. |
| `nfpr` | `string` | No | `0` | Exclude auto-corrected results: `0` or `1`. |
| `filter` | `string` | No | `0` | Filter duplicate results: `0` or `1`. |
| `max_pages` | `integer` | No | `1` | Maximum pages to fetch (`0` = no limit). Each page is billed separately. |
| `output_file` | `string` | No | (none) | Optional filename to save results. |

## Output Format

A real result for `best coffee brewing methods` (one item per page; snippets are trimmed here for readability).

```json
{
  "search_parameters": {
    "q": "best coffee brewing methods",
    "location": null,
    "gl": "us",
    "hl": "en",
    "safe": "off",
    "device": "desktop",
    "max_pages": 1
  },
  "search_metadata": {
    "total_results": 10,
    "forums_count": 10,
    "pages_processed": 1,
    "max_pages_set": 1,
    "pagination_limit_reached": true
  },
  "search_information": {
    "organic_results_state": "Results for exact spelling"
  },
  "page_number": 1,
  "forum_results": [
    {
      "position": 1,
      "title": "What's your favorite brewing method? : r/Coffee",
      "link": "https://www.reddit.com/r/Coffee/comments/666cbs/whats_your_favorite_brewing_method/",
      "displayed_meta": "20+ comments · 9 years ago",
      "snippet": "I highly recommend the AeroPress for your first brewer. It's practically a giant syringe/plunger with a filter on the end.",
      "source": "Reddit · r/Coffee"
    },
    {
      "position": 2,
      "title": "Best coffee brewing methods",
      "link": "https://www.facebook.com/groups/foodiessofl/posts/2826219634377953/",
      "displayed_meta": "10+ comments · 1 month ago",
      "snippet": "My preferred methods are espresso and cold brew. Sometimes I do Aeropress.",
      "source": "Facebook · Foodies Who Review South Florida"
    }
  ]
}
```

---

## Use as an MCP tool

You can load the Google Forums API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Forums API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Forums API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Forums API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/google-forums-search-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api`, using OAuth when prompted.
5. Ask Claude to run the Google Forums API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Forums API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/google-forums-search-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Forums API to power sentiment analysis, research, and AI workflows with reliable, structured results.*

Last Updated: 2026.07.12
