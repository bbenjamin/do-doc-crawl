from crawler.crawler import Crawler
from config.config import CrawlerConfig
from utils.json_helper import write_json_to_file, create_hierarchical_json_tree

if __name__ == "__main__":
    crawler = Crawler(CrawlerConfig.START_URL, CrawlerConfig.MAX_DEPTH, CrawlerConfig.INTERNAL_LINK_SELECTOR)
    crawler.start_crawling()
    print('done crawling')
    link_tree = crawler.get_link_tree()
    print(link_tree)
    # json = create_hierarchical_json_tree(link_tree)
    write_json_to_file(link_tree, CrawlerConfig.OUTPUT_FILE)
