from os import environ, makedirs, path
from urllib.parse import urlparse

import twisted.python.failure
from scrapy import Request, Spider
from scrapy_playwright.page import PageMethod


class ScrollSpider(Spider):
    """Scroll down on an infinite-scroll page."""

    name = "scroll54"
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "LOG_LEVEL": "INFO",
    }

    # allowed_domains = ["toscrape.com"]
    # start_urls = ["http://quotes.toscrape.com/scroll"]
    root_dir = environ.get(
        "ROOT_DIR",
        path.join(
            path.dirname(path.dirname(path.dirname(path.dirname(__file__)))),
            "downloaded",
        ),
    )

    def parse(self, response, **kwargs):
        print("ScrollSpider::parse")
        if isinstance(response, twisted.python.failure.Failure):
            return {
                "error": str(response),
                "brief_traceback": response.getBriefTraceback().splitlines(),
                "traceback": response.getTraceback().splitlines(),
            }

        parsed_url = urlparse(response.url)
        directory = path.join(self.root_dir, "screenshots", parsed_url.hostname)
        print("ScrollSpider::parse::directory:", repr(directory), ";")
        makedirs(directory, exist_ok=True)
        yield Request(
            url=response.url,
            cookies={"foo": "bar", "asdf": "qwerty"},
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "div.quote"),
                    PageMethod(
                        "evaluate", "window.scrollBy(0, document.body.scrollHeight)"
                    ),
                    PageMethod(
                        "wait_for_selector", "div.quote:nth-child(11)"
                    ),  # 10 per page
                    PageMethod(
                        "screenshot",
                        path=path.join(directory, "scroll.png"),
                        full_page=True,
                    ),
                ],
            },
        )

        return {"url": response.url, "count": len(response.css("div.quote"))}


__all__ = ["ScrollSpider"]
