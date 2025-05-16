# Drupal Docs Crawler

This project is a web crawler designed to extract internal links from the Drupal documentation site. It creates a hierarchical JSON tree of all internal links within the `#block-system-main` section, crawling through 12 levels of nesting.

## Project Structure

```
drupal-docs-crawler
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── crawler
│   │   ├── __init__.py
│   │   ├── crawler.py
│   │   └── parser.py
│   ├── config
│   │   ├── __init__.py
│   │   └── config.py
│   └── utils
│       ├── __init__.py
│       ├── url_helper.py
│       └── json_helper.py
├── output
│   └── .gitkeep
├── tests
│   ├── __init__.py
│   ├── test_crawler.py
│   └── test_parser.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd drupal-docs-crawler
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the crawler, execute the following command:
```
python src/main.py
```

This will start the crawling process from the specified `START_URL` in the configuration file and generate a JSON output of the internal links.

## Configuration

The crawler's behavior can be configured in the `src/config/config.py` file. You can adjust parameters such as:
- `START_URL`: The URL where the crawler begins.
- `MAX_DEPTH`: The maximum depth of crawling (default is 12).
- `INTERNAL_LINK_SELECTOR`: The CSS selector used to find internal links.

## Testing

Unit tests are provided to ensure the functionality of the crawler and parser. To run the tests, use:
```
pytest tests/
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.