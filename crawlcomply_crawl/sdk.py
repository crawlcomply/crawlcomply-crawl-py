from copy import deepcopy

from twisted.internet import pollreactor

pollreactor.install()
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from crawlcomply_crawl.crawlcomply_scraper.crawlcomply_scraper.spiders.scroll import (
    ScrollSpider,
)


def crawl(start_urls, allowed_domains):
    cls = deepcopy(ScrollSpider)
    cls.start_urls = start_urls
    cls.allowed_domains = allowed_domains

    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(cls)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run(installSignalHandlers=0)
    return "scraped"
