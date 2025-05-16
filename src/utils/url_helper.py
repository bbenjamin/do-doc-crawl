def is_internal_url(base_url, url):
    from urllib.parse import urlparse, urljoin

    parsed_base = urlparse(base_url)
    parsed_url = urlparse(url)

    return parsed_url.netloc == parsed_base.netloc

def construct_full_url(base_url, relative_url):
    return urljoin(base_url, relative_url)