class CrawlerConfig:
    # Starting URL for the crawler
    START_URL = 'https://www.drupal.org/docs/administering-a-drupal-site'

    # Maximum depth of links to crawl (12 levels of nesting)
    MAX_DEPTH = 8

    # CSS selector to find internal links within the main content block
    INTERNAL_LINK_SELECTOR = '#block-system-main .pane-content a[href^="/"]'

    # Output file path
    OUTPUT_FILE = 'output/drupal_headings_administering.json'

    # Request headers to mimic a browser
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

    # Delay between requests (in seconds) to be respectful to the server
    REQUEST_DELAY = 1
