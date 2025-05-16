from .parser import Parser


class Crawler:
    def __init__(self, start_url, max_depth, internal_link_selector):
        self.start_url = start_url
        self.max_depth = max_depth
        self.internal_link_selector = internal_link_selector
        self.visited_links = set()
        self.link_tree = {}
        self.parser = Parser()

    def crawl(self, url, depth):
        if depth > self.max_depth:
            return

        self.visited_links.add(url)
        print('Crawling ' + url + ' At depth ' + str(depth))
        links = self.extract_links(url)

        for link in links:
            self.link_tree[url] = self.link_tree.get(url, [])
            self.link_tree[url].append(link)
            self.crawl(link['href'], depth + 1)

    def extract_links(self, url):
        return self.parser.extract_links(url, self.visited_links, self.start_url)

    def get_link_tree(self):
        return self.link_tree

    def start_crawling(self):
        return self.crawl(self.start_url, 0)
